#! C:\Python27\python.exe

print "Content-Type: text/html\n"

from os.path import join,abspath
import cgi,sys,sha

BASE_DIR = abspath('data')

form = cgi.FieldStorage()

text = form.getvalue('text')
filename = form.getvalue('filename')
password = form.getvalue('password')

if not (filename and text and password):
    print 'Invalid parameters'
    sys.exit()

if sha.sha(password).hexdigest() != '01c3bde0':
    print 'Invalid parameters'
    sys.exit()

f = open(join(BASE_DIR,filename), 'w')
f.write(text)
f.close()

print 'The file has been saved.'