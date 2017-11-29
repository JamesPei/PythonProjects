# -*-coding:utf-8-*-

import cookielib
import urllib
import urllib2

ID_USERNAME = ''
ID_PASSWORD = ''
USERNAME = ''
PASSWORD = ''
LOGIN_URL = ''
NORMAL_URL = ''


def extract_cookie_info():
    # set up cookie jar
    cj = cookielib.CookieJar()
    login_data = urllib.urlencode({ID_USERNAME: USERNAME, ID_PASSWORD: PASSWORD})
    # create url opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    resp = opener.open(LOGIN_URL, login_data)

    # send login info
    for cookie in cj:
        print '----First time cookie: %s--->%s' % (cookie.name, cookie.value)

    print 'Headers: %s' % resp.headers

    # now access without any login info
    resp = opener.open(NORMAL_URL)
    for cookie in cj:
        print '++++Send time cookie: %s--->%s' % (cookie.name, cookie.value)

    print 'Headers: %s' % resp.headers

if __name__ == '__main__':
    extract_cookie_info()