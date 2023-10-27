from flask import Blueprint, render_template, Response, session, request, flash, url_for, redirect
import re
from werkzeug.security import generate_password_hash, check_password_hash
from .models import *
from datetime import datetime
from . import db

DB_NAME = "mess_management.db"

user_functions = Blueprint('user_functions', __name__)

@user_functions.route('/attendance', methods=['GET', 'POST'])
def mark_absent():
    user_MIS = session["name"]
    today = datetime.now()
    year = today.year
    month = today.month
    date = today.day
    lunch = ""
    dinner = ""

    if request.method == 'POST':
        meal_time = request.form.getlist('meal_time')
        if len(meal_time) > 1:
            if meal_time[0] == 'Lunch':
                lunch = date
            if meal_time[1] == 'Dinner':
                dinner = date
                print(date)
        elif len(meal_time) == 1:
            if meal_time[0] == 'Lunch':
                lunch = date
            if meal_time[0] == 'Dinner':
                dinner = date
                print(date)

        mark_absent = Attendance(user_MIS=user_MIS, Year=year, Month=month, Lunch=lunch, Dinner=dinner)
        db.session.add(mark_absent)
        db.session.commit()

        payment_records()
        flash('Absentee Marked', category='success')
        return redirect(url_for('views.user_dashboard'))

    return render_template("mark_absentee.html", boolean=True)


@user_functions.route('/present')
def present_records():
    user_MIS = session["name"]

    students = student_info.query.filter(student_info.MIS == user_MIS).all()
    attendees = Attendance.query.filter(Attendance.user_MIS == user_MIS).all()

    return render_template('present_records.html', curr_name=user_MIS, dataOfStudents=students, data_of_absentees=attendees)


@user_functions.route('/payment', methods=['GET', 'POST'])
def payment_records():
    user_MIS = session["name"]

    students = student_info.query.all()

    # Filter attendees based on user_MIS
    attendees = Attendance.query.filter(Attendance.user_MIS == user_MIS).all()

    count = 0

    for attendee in attendees:
        if attendee.Lunch == "":
            count += 1
        if attendee.Dinner == "":
            count += 1

    payment_rec = Payment(user_MIS=user_MIS, noOfMeals=count, total=count * 50)
    db.session.add(payment_rec)
    db.session.commit()

    data = student_info.query.all()

    return render_template('payment_records.html', data=students, data_of_absentees=attendees)
