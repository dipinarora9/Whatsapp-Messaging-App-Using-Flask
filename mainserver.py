#! python3
'''
Created on 21-Oct-2018

@author: Dipin Arora
'''

import os
from functools import wraps

from flask import Flask, request, redirect, url_for, render_template, session, flash

import gmail
import whatsappmsg

from forms import LoginForm, RegisterForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.urandom(12)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///allData.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#
# if 'userData.db' is None:
#     print('Creating Database')
#     db.create_all()

from model import Table

if Table.query.filter_by(username='admin', password='admin').first() is None:
    admin = Table(username='admin', password='admin', email='admin@gmail.com', phoneNo='123456789')
    db.session.add(admin)
    db.session.commit()


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("You need to LogIn First")
            return redirect("/")

    return wrap


@app.route("/")
def welcome():
    car = None
    return render_template("welcome.html", car=car)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        user = Table.query.filter_by(username=form.username.data, password=form.password.data).first()
        if user is not None:
            session["logged_in"] = True
            flash("You were logged In!")
            return redirect(f"/whatsapp/{user.id}")
        else:
            return "Invalid Credentials. Please try again"

    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    session.pop("logged_in", None)
    flash("You were logged Out!")
    return redirect(url_for("welcome"))


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        gmail.mail(form.email.data, form.username.data)
        newUser = Table(username=form.username.data, email=form.email.data, password=form.password.data,
                        phoneNo=form.number.data)

        try:
            db.session.add(newUser)
            db.session.commit()
            flash("You are Registered Server Side. Please check your mail for further instructions.")

            return redirect('/login')
        except:
            return 'error saving name'

    return render_template('register.html', form=form)


@app.route("/whatsapp/<int:id>", methods=['GET', 'POST'])
@login_required
def whatsapp(id):
    receivedMsg = ''
    user = Table.query.filter_by(id=id).first()
    twilionNum = os.environ.get('twilioNo')
    if request.method == "POST":
        try:
            whatsappmsg.send_message(user.phoneNo, request.form['mes'])
            receivedMsg = whatsappmsg.read_message(user.phoneNo)
        except:
            redirect('/whatsapp')
    else:
        pass
    if receivedMsg == '': receivedMsg = 'No previous message'
    return render_template("whatsappmsgs.html", currentUser=user, receivedMsg=receivedMsg, twilionNum=twilionNum)


if __name__ == "__main__":
    app.run(debug=True)
