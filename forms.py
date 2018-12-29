'''
Created on 21-Oct-2018

@author: Dipin Arora
'''
from flask_wtf import Form

from wtforms import TextField, PasswordField, IntegerField

from wtforms.validators import DataRequired, Length, Email, EqualTo





class LoginForm(Form):

    username = TextField('Username', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])





class RegisterForm(Form):

    username = TextField(

        'username',

        validators=[DataRequired(), Length(min=3, max=25)]

    )

    email = TextField(

        'email',

        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]

    )
    
    number = IntegerField(

        'number',

        validators=[DataRequired()]

    )

    password = PasswordField(

        'password',

        validators=[DataRequired(), Length(min=5, max=25)]

    )

    confirm = PasswordField(

        'Repeat password',

        validators=[

            DataRequired(), EqualTo('password', message='Passwords must match.')

        ]

    )
    
    

class num_and_msg(Form):
    
    num = IntegerField("num", validators=[DataRequired()])
    
    mes = TextField("message", validators=[DataRequired()])
    
