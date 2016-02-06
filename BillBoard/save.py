#! C:\Python27\python.exe
# -*- coding:utf-8 -*-

print "Content-Type: text/html\n"

import cgitb; cgitb.enable()

def quote(string):
    if string:
        return string.replace("'","\\'")
    else:
        return string

import sqlite3
conn = sqlite3.connect('messages.db')
curs = conn.cursor()
import cgi,sys
form = cgi.FieldStorage()

sender = quote(form.getvalue('sender'))
subject = quote(form.getvalue('subject'))
text = quote(form.getvalue('text'))
reply_to = form.getvalue('reply_to')

if not (sender and subject and text):
    print 'Please supply sender,subject,and text'
    sys.exit()

if reply_to is not None:
    query = """insert into messages(reply_to,sender,subject,text) VALUES (%i,'%s','%s','%s')""" % (int(reply_to),sender,subject,text)
else:
    print 2,sender,subject,text
    query = """insert into messages(sender,subject,text) VALUES ('%s','%s','%s') """ % (sender,subject,text)

curs.execute(query)
conn.commit()

print """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Message Saved</title>
    </head>
    <body>
        <h1>Message Saved</h1>
        <hr/>
        <a href='main.py'>Back to Main Page</a>
    </body>
</html>
"""
