#__author__ = 'James'
#-*- coding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('messages.db')
curs = conn.cursor()

# curs.execute('''
# CREATE TABLE messages(
#   id integer primary KEY AUTOINCREMENT ,
#   subject TEXT NOT NULL ,
#   sender TEXT NOT NULL ,
#   reply_to int,
#   text text NOT NULL
# )
# ''')

# query = 'insert into messages(sender,subject,reply_to,text) values(?,?,?,?)'
# curs.execute(query,['admin','python',1,'lets talk about python'])

curs.execute('select * from messages')
rows = curs.fetchall()
print rows

conn.commit()
conn.close()