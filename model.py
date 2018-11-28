from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Submission(Base):
    __tablename__ = 'Submission'
    id = Column(Integer, primary_key=True)
    user_name= Column(String(200))
    assignment_id = Column(Integer)
    course_id = Column(Integer)
    submitted_code = Column(String(5000))
    num_passed= Column(Integer)
    num_failed= Column(Integer)
    num_pass_required= Column(Integer)
    results= Column(String(200))
    checked = Column(Boolean(), nullable=False, default=False)
    num_lines_code=Column(Integer)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Submission {0!r}>'.format(self.user_name)

    @staticmethod
    def by_id(name):
        return Submission.query.filter_by(id=id)

    def get_assignment_id(assignment_id):
        return Submission.query.filter_by(assignment_id=assignment_id)

    def by_user_name(name):
        return Submission.query.filter_by(user_name=name)

    def by_course_id(id):
        return Submission.query.filter_by(course_id=id)
