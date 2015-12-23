#! C:\Python27\python.exe

print "Content-Type: text/html\n"

from os.path import join,abspath
import cgi,sys

BASE_DIR = abspath('data')      #获取data目录的绝对路径

form = cgi.FieldStorage()
filename = form.getvalue('filename')
if not filename:
    print 'Please enter a file name'
sys.exit()
text = open(join(BASE_DIR, filename)).read()
print """
<html>
    <head>
        <meta charset="UTF-8">
        <title>Editing...</title>
    </head>
    <body>
        <form action='/cgi-bin/save.cgi' method='POST'>
            <b>File:</b>%s<br/>
            <input type='hidden' value='%s' name='filename'/>
            <b>Password:</b>%s<br/>
            <input type='password' name='password'/><br/>
            <b>Text:</b>%s<br/>
            <textarea name='text' cols='40' rows='20'>%s</textarea><br/>
            <input type='submit' value='Save'/><br/>
        </form>
    </body>
</html>
"""%(filename,filename,text)