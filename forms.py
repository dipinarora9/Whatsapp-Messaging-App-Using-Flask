'''
Created on 21-Oct-2018

@author: Dipin Arora
'''
from flask_wtf import Form

from wtforms import StringField, PasswordField, IntegerField

from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(Form):
    username = StringField(

        'username',

        validators=[DataRequired(), Length(min=3, max=25)]

    )

    email = StringField(

        'email',

        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]

    )

    number = IntegerField(

        'number',

        validators=[DataRequired()]

    )

    password = PasswordField(

        'password',

        validators=[DataRequired(), Length(min=5, max=20)]

    )

    confirm = PasswordField(

        'Repeat password',

        validators=[

            DataRequired(), EqualTo('password', message='Passwords must match.')

        ]

    )


