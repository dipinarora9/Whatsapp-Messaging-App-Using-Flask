'''
Created on 21-Oct-2018

@author: Home
'''



import sqlite3
#with sqlite3.connect('login.db') as connection:
    
connection=sqlite3.connect("login.db")

cursor=connection.cursor()
sql_command = """CREATE TABLE login ( username VARCHAR(25),  email VARCHAR(40),  password VARCHAR(25),    phone_number    INT(10)) ;"""
cursor.execute(sql_command)
connection.commit()
connection.close()