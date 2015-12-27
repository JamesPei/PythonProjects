#! C:\Python27\python.exe
# -*- coding:utf-8 -*-

print "Content-Type: text/html\n"

from os.path import join,abspath
import cgi,sys,sha

BASE_DIR = abspath('C:\Program Files (x86)\Apache Software Foundation\Apache2.2\cgi-bin\data')

form = cgi.FieldStorage()

text = form.getvalue('text')
filename = form.getvalue('filename')
password = form.getvalue('password')

if not (filename and text and password):
    print 'Invalid parameters'
    sys.exit()
#password:123
if sha.sha(password).hexdigest() != '40bd001563085fc35165329ea1ff5c5ecbdbbeef':
    print 'Invalid parameters'
    sys.exit()

f = open(join(BASE_DIR,filename), 'w')
f.write(text)
f.close()

print 'The file has been saved.'