#! C:\Python27\python.exe
# -*- coding:utf-8 -*-

print "Content-Type: text/html\n"

import cgitb; cgitb.enable()

import sqlite3

conn = sqlite3.connect('messages.db')
curs = conn.cursor()

import cgi,sys
form = cgi.FieldStorage()
id = form.getvalue('id')

print """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>View Message</title>
    </head>
    <body>
        <h1>View Message</h1>
"""

try:id = int(id)
except:
    print 'Invalid mesage ID'
    sys.exit()

curs.execute('select * from messages where id=%i' % id)
rows = curs.fetchall()

if not rows:
    print 'Unknown message ID'
    sys.exit()

row = rows[0]

print """
        <p>
            <b>Subject:</b>%s<br/>
            <b>Sender:</b>%s<br/>
            <pre>%s</pre>
        </p>
        <hr/>
        <a href='main.py'>Back to the main page</a>
        <a href='edit.py?reply_to=%i'>Reply</a>
    </body>
</html>
""" % (row[3],row[2],row[4],row[0])

