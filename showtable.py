'''
Created on 21-Oct-2018

@author: Home
'''
import sqlite3
#with sqlite3.connect('login.db') as connection:
    
connection=sqlite3.connect("login.db")

cursor=connection.cursor()
sql_command = """SELECT * FROM login ;"""
cursor.execute(sql_command)
connection.commit()
connection.close()