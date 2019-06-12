'''
Created on 21-Oct-2018

@author: Dipin Arora
'''

from mainserver import db
import datetime

class Table(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    phoneNo = db.Column(db.Integer, nullable=False)
    dateAdded = db.Column(db.DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return '<User %r>' % self.username
