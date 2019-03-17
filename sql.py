'''
Created on 21-Oct-2018

@author: Dipin Arora
'''

import sqlite3

connection = sqlite3.connect("login.db")

cursor = connection.cursor()
sql_command = """CREATE TABLE login ( username VARCHAR(25),  email VARCHAR(40),  password VARCHAR(25),    phone_number    INT(10)) ;"""
cursor.execute(sql_command)
cursor.execute('''INSERT INTO login VALUES ("admin", "admin@admin.com", "admin", "1234567890")''')
connection.commit()
connection.close()
