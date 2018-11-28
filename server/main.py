from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from login import *
engine = create_engine('sqlite:///users.db', echo=True)
Base = declarative_base()


app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
        # what are all the semesters
        # 
        return render_template('home.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()

    # if user is a student
        # Session['user']='student'
    #if user is a teacher
        # session['user']='teacher'

    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

# list of all the semester for the user to choose from
@app.route("/semesters")
def semesters():
    return render_template("semesters.html")

# update cources bases on the semester and user
@app.route("/cources", methods=['POST'])
def cources():
    return render_template("cources.html")

# display assignments based on cource selection and the user
@app.route("/assignments", methods=['POST'])
def assignments():
    return render_template("assignments.html")

# details of an assignment based on the input from the user
@app.route("/assignment", methods=['POST'])
def assignment():
    return render_template("assignment.html")

# submit an assignment based assignment and the user.
@app.route("/submit", methods=['POST'])
def submit():
    return render_template("submit.html")


@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
