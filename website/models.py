from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

defaultmonth=currentMonth = datetime.now().month
defaultyear=currentMonth = datetime.now().year


# class Payment(db.Model):
#     ID=db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_MIS=db.Column(db.String(50),db.ForeignKey('student_info.MIS'))
#     noOfMeals=db.Column(db.Integer)
#     total=db.Column(db.Integer)
    

class Attendance(db.Model):
    user_MIS = db.Column(db.String(50), db.ForeignKey('student_info.MIS', ondelete='CASCADE'))
    ID=db.Column(db.Integer, primary_key=True, autoincrement=True)
    Year=db.Column((db.String(50)),default=defaultyear)
    Month=db.Column((db.String(50)),default=defaultmonth)
    Lunch=db.Column(db.String(10))
    Dinner=db.Column(db.String(10))

class student_info(db.Model, UserMixin):
    Name = db.Column(db.String(50), nullable=False)
    MIS = db.Column(db.String(50), primary_key=True, nullable=False)
    year=db.Column(db.String(50), nullable=False)
    Room_no = db.Column(db.String(50), nullable=False)
    Phone_no = db.Column(db.String(10), nullable=False)
    Password = db.Column(db.String(50), nullable=False)
    notes=db.relationship('Attendance')
    # payment=db.relationship('Payment')








    
    
