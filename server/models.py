from werkzeug.exceptions import BadRequest

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, MetaData, types
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import aliased, backref
from sqlalchemy.sql import text

from markdown import markdown
import pytz

import functools

from collections import namedtuple, Counter

import contextlib
import csv
import datetime as dt
import json
import os
import logging
import shlex
import urllib.parse
import mimetypes

from server.constants import (VALID_ROLES, STUDENT_ROLE, STAFF_ROLES, TIMEZONE,
                              SCORE_KINDS, OAUTH_OUT_OF_BAND_URI,
                              INSTRUCTOR_ROLE, ROLE_DISPLAY_NAMES)

from server.extensions import cache, storage
from server.utils import (encode_id, chunks, generate_number_table,
                          humanize_name)
logger = logging.getLogger(__name__)

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)

def transaction(f):
    @functools.wraps(f)
    def wrapper(*args, **kwds):
        try:
            value = f(*args, **kwds)
            db.session.commit()
            return value
        except:
            db.session.rollback()
            raise
    return wrapper

class Json(types.TypeDecorator):
    impl = types.Text

    def process_bind_param(self, value, dialect):
        # Python -> SQL
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        # SQL -> Python
        return json.loads(value)

sclass Timezone(types.TypeDecorator):
    impl = types.String(255)

    def process_bind_param(self, value, dialect):
        # Python -> SQL
        if not hasattr(value, 'zone'):
            if value not in pytz.common_timezones_set:
                logger.warning('Unknown TZ: {}'.format(value))
                # Unknown TZ, use default instead
                return TIMEZONE
            return value
        return value.zone

    def process_result_value(self, value, dialect):
        # SQL -> Python
        return pytz.timezone(value)
    def process_result_value(self, value, dialect):
        """ SQL -> Python
        Uses shlex.split to handle values with spaces.
        It's a fragile solution since it will break in some cases.
        For example if the last character is a backslash or otherwise meaningful
        to a shell.
        """
        values = []
        for val in shlex.split(value):
            if " " in val and '"' in val:
                values.append(val[1:-1])
            else:
                values.append(val)
        return values

class Model(db.Model):
    """ Timestamps all models, and serializes model objects."""
    __abstract__ = True

    created = db.Column(db.DateTime(timezone=True),
                        server_default=db.func.now(), nullable=False)

    def __repr__(self):
        if hasattr(self, 'id'):
            key_val = self.id
        else:
            pk = self.__mapper__.primary_key
            if type(pk) == tuple:
                key_val = pk[0].name
            else:
                key_val = self.__mapper__.primary_key._list[0].name
        return '<{0} {1}>'.format(self.__class__.__name__, key_val)

    @classmethod
    def can(cls, obj, user, action):
        if user.is_admin:
            return True
        return False

    @hybrid_property
    def export(self):
        """ CSV export data. """
        if not hasattr(self, 'export_items'):
            return {}
        return {k: v for k, v in self.as_dict().items() if k in self.export_items}

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def from_dict(self, dict):
        for c in self.__table__.columns:
            if c.name in dict:
                setattr(self, c.name, dict[c.name])
        return self

class User(Model, UserMixin):
    id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False, index=True, primary_key=True)
    is_admin = db.Column(db.Boolean(), default=False)
    course_enrolled = db.Column(db.String(255))

    export_items = ('email', 'name')

    def __repr__(self):
        return '<User {0}>'.format(self.email)

    def enrollments(self):
        query = (Enrollment.query.join(Enrollment.course)
                           .filter(Enrollment.user_id == self.id)
        return query.all()

    @cache.memoize(120)
    def is_enrolled(self, course_id):
        query = (Enrollment.query.join(Enrollment.course)
                           .options(db.contains_eager(Enrollment.course))
                           .filter(Enrollment.user_id == self.id)
                           .filter(Enrollment.course_id== course_id)
        if query == '':
            return False
        return True

    @hybrid_property
    def identifier(self):
        return humanize_name(self.name) or self.email

    @cache.memoize(3600)
    def num_grading_tasks(self):
        return GradingTask.query.filter_by(grader=self, score_id=None).count()

    def is_staff(self):
        if self.is_admin:
            return True
        return False

    @staticmethod
    def get_by_id(uid):

        return User.query.get(uid)

    @staticmethod
    @cache.memoize(240)
    def email_by_id(uid):
        user = User.query.get(uid)
        if user:
            return user.email

    @staticmethod
    def lookup(email):

        return User.query.filter_by(email=email).one_or_none()

class Semester(Model):
    name = db.Column(db.String(255), primary_key=True)



    def __repr__(self):
        return '<Assignment {0!r}>'.format(self.offering)

    @staticmethod
    def get_all_semesters():
        return Semesters.all()

    def add_semester(assignment_id):
        # see if user is an admin
        return Submission.query.filter_by(assignment_id=assignment_id).one_or_none()


class Course(Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True, index=True)
    institution = db.Column(db.String(255), nullable=False)  # E.g., 'UC Berkeley'
    display_name = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255))
    active = db.Column(db.Boolean(), nullable=False, default=True)
    timezone = db.Column(Timezone, nullable=False, default=pytz.timezone(TIMEZONE))
    semester= db.Column(db.String(255), nullable= False)

    @classmethod
    def can(cls, obj, user, action):
        if user.is_admin:
            return True
        if not obj:
            return False
        if action == "view":
            return user.is_authenticated
        return user.is_enrolled(obj.id, STAFF_ROLES)

    def __repr__(self):
        return '<Course {0!r}>'.format(self.offering)

    @staticmethod
    def by_name(name):
        return Course.query.filter_by(offering=name).one_or_none()

    def by_id(id):
        return Course.query.filter_by(id=id)

    @property
    def display_name_with_semester(self):
        return self.display_name + " " + Course.query.filter_by(self.id).semester

    def statistics(self):
        assignments = self.assignments
        active_assignments = [x for x in assignments if x.active]
        inactive_assignments = [x for x in assignments if not x.active]

        backup_count_query = (Backup.query.join(Backup.assignment)
                                    .filter(Assignment.course == self))

        count_by_role = dict(Counter([x.role for x in self.participations]))

        count_by_role['all_staff'] = sum(count_by_role.get(x, 0) for x in STAFF_ROLES)

        return {
            'active_assignments': len(active_assignments),
            'inactive_assignments': len(inactive_assignments),
            'backup_count': backup_count_query.count(),
            'submit_count': backup_count_query.filter(Backup.submit == True).count(),
            'enrollment_counts': count_by_role
        }


    def is_enrolled(self, user_id):
        return Enrollment.query.filter_by(
            user_id=user_id,
            course_id=self.course_id,
            staff= False
        ).count() > 0

    def get_participants(self, course_id, staff):
        return (Enrollment.query
                          .options(db.joinedload('user'))
                          .filter(Enrollment.staff = staff,
                                  Enrollment.course_id == self.id)
                          .all())

    def get_staff(self, course_id):
        return self.get_participants(course_id, staff= True)

    def get_students(self):
        return self.get_participants(course_id, staff= False)

    def initialize_content(self, user):
        """ When a course is created, add the creating user as an instructor
        and then create an example assignment.
        """
        enroll = Enrollment(course=self, user_id=user.id, role=INSTRUCTOR_ROLE)
        assign = Assignment(course_id=self, display_name="Example",
                            name=self.offering + '/example',
                            max_group_size=2, uploads_enabled=True,
                            due_date=dt.datetime.now() + dt.timedelta(days=7),
                            lock_date=dt.datetime.now() + dt.timedelta(days=8))
        db.session.add_all([enroll, assign])
        db.session.commit()


class Assignment(Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True, index=True)
    display_name = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), nullable=False, default=True)
    timezone = db.Column(Timezone, nullable=False, default=pytz.timezone(TIMEZONE))
    course_id= db.Column(db.String(255), nullable=False)
    num_of_students= db.Column(db.Integer)
    due_date= db.Column(DateTime)
    max_group _size= db.Column(db.Integer)


    def __repr__(self):
        return '<Assignment {0!r}>'.format(self.offering)

    @staticmethod
    def by_name(name):
        return Assignment.query.filter_by(offering=name).one_or_none()

    def get_by_courseid(course_id):
        return Assignment.query.filter_by(course_id=course_id).one_or_none()

    def by_id(id):
        return Assignment.query.filter_by(id=id)

class Enrollment(Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    course_id = db.Column(db.Integer)
    staff = db.Column(db.Boolean(), nullable=False, default=False)


    def __repr__(self):
        return '<Assignment {0!r}>'.format(self.offering)

    @staticmethod
    def by_id(name):
        return Assignment.query.filter_by(id=id).one_or_none()

    def get_course_id(course_id):
        return Assignment.query.filter_by(course_id=course_id).one_or_none()

    def by_user_id(id):
        return Assignment.query.filter_by(user_id=user_id).one_or_none()

class Submission(Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    assignment_id = db.Column(db.Integer)
    course_id = db.Column(db.Integer)
    submitted_code = name = db.Column(db.String(5000))
    results= db.Column(db.String(200))


    def __repr__(self):
        return '<Assignment {0!r}>'.format(self.offering)

    @staticmethod
    def by_id(name):
        return Submission.query.filter_by(id=id).one_or_none()

    def get_assignment_id(assignment_id):
        return Submission.query.filter_by(assignment_id=assignment_id).one_or_none()

    def by_user_id(id):
        return Assignment.query.filter_by(user_id=user_id).one_or_none()

    def by_course_id(id):
        return Assignment.query.filter_by(course_id=user_id).one_or_none()

    def by_user_assignment_id(user_id, assignment_id):
        return Assignment.query.filter_by(user_id=user_id).filter_by(assignment_id=assignment_id).one_or_none()
