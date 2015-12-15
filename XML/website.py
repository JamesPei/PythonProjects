#__author__ = 'James'
#-*- coding:utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import parse
import os

class Dispatcher:

    def dispatch(self, prefix, name, attrs=None):
        mname = prefix + name.capitalize()
        dname = 'default'+prefix.capitalize()
        method = getattr(self, mname, None)
        if callable(method): args = ()
        else:
            method = getattr(self,dname,None)
            args = name,
        if prefix == 'start': args += attrs,
        if callable(method):method(*args)



