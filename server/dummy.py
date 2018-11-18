import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from login import *

engine = create_engine('sqlite:///users.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin","password")
session.add(user)



session.commit()
