'''
Created on 21-Oct-2018

@author: Dipin Arora
'''


from flask import Flask, request, redirect,url_for, render_template, session,flash
import gmail, whatsappmsg
from functools import wraps
from forms import LoginForm, RegisterForm, num_and_msg
import sqlite3




conn=sqlite3.connect("login.db")
cur=conn.cursor()

app = Flask(__name__)
app.secret_key="dipin"

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
def Welcome():
    Car=None
    return render_template("welcome.html",Car=Car)





@app.route("/login",methods=["GET","POST"])
def login():
    conn=sqlite3.connect("login.db")
    cur=conn.cursor()
    error=None
    form=LoginForm(request.form)
    if request.method == "POST":
        user = cur.execute("SELECT username FROM login;")
        username=user.fetchall()
        passw=cur.execute("SELECT password FROM login")
        password=passw.fetchall()
        for i in username:
            for j in password:
                if form.username.data==i[0] and form.password.data==j[0]:
                    session["logged_in"]=True
                    flash("You were logged In!")
                    return redirect("/whatsapp")
                else:
                    pass

        else:
            error="Invalid Credentials. Please try again"
               
    return render_template("login.html", form=form, error=error)





@app.route('/logout')
@login_required
def logout():
    session.pop("logged_in",None)
    flash("You were logged Out!")
    return redirect(url_for("Welcome"))
    





@app.route("/register",methods=['GET','POST'])
def register():
    conn=sqlite3.connect("login.db")
    cur=conn.cursor()
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        gmail.mail(form.email.data,form.username.data)

        cur.execute(""" INSERT INTO login VALUES (?,?,?,?)""",(form.username.data,form.email.data,form.password.data,form.number.data))

        conn.commit()
        conn.close()
        flash("You are Registered Server Side. Please check your mail for further instructions.")

        return redirect('/login')

    return render_template('register.html', form=form)
    



       
             
@app.route("/whatsapp", methods=['GET', 'POST'])
@login_required
def whatsapp():
    car=None
    msg=''
    form=num_and_msg(request.form)
    if request.method=="POST":
        msg=whatsappmsg.read_message(form.num.data)
        whatsappmsg.send_message(form.num.data, form.mes.data)
        print(form.mes)
    else:
        pass
    return render_template("whatsappmsgs.html",form=form ,car=car, msg=msg)
    

   
    



if __name__ == "__main__":
    app.run(debug=True)


