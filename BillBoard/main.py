#! C:\Python27\python.exe
# -*- coding:utf-8 -*-

print "Content-Type: text/html\n"

import cgitb; cgitb.enable()
import sqlite3

conn = sqlite3.connect('messages.db')
curs = conn.cursor()

print """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>BillBoard</title>
    </head>
    <body>
        <h1>BillBoard</h1>
"""

curs.execute('select * from messages')
rows = curs.fetchall()
toplevel = []
children = {}

for row in rows:
    parent_id = row[3]      #reply_to
    if parent_id is None:
        toplevel.append(row)
    else:
        children.setdefault(parent_id,[]).append(row)

def format(row):
    print '<p><a href="view.py?id=%i">%s</a></p>' % (row[0],row[1])
    try:kids = children[row[0]]
    except KeyError:pass
    else:
        print '<blockquote>'
        for kid in kids:
            format(kid)
        print '</blockquote>'

print '<p>'

for row in toplevel:
    format(row)

print """
        </p>
        <hr/>
            <p><a href="edit.py">Post message</a></p>
    </body>
</html>
"""


