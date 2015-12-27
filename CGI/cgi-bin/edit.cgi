#! C:\Python27\python.exe
# -*- coding:utf-8 -*-

print "Content-Type: text/html\n"

from os.path import join,abspath
import cgi,sys

BASE_DIR = abspath('C:\Program Files (x86)\Apache Software Foundation\Apache2.2\cgi-bin\data')      #获取data目录的绝对路径

form = cgi.FieldStorage()
filename = form.getvalue('filename')

if not filename:
    print 'Please enter a file name'
	sys.exit()
	
text = open(join(BASE_DIR, filename)).read()
print """
<html>
    <head>
        <title>Editing...</title>
    </head>
    <body>
        <form action='save.cgi' method='POST'>
            <b>File:</b>%s<br/>
            <input type='hidden' value='%s' name='filename'/>
            <b>Password:</b><br/>
            <input type='password' name='password'/><br/>
            <b>Text:</b><br/>
            <textarea name='text' cols='40' rows='20'>%s</textarea><br/>
            <input type='submit' value='Save'/><br/>
        </form>
    </body>
</html>
"""%(filename,filename,text)