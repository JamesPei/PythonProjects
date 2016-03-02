#__author__ = 'James'
#-*-coding:utf-8-*-

import pymongo
import datetime
import random

#创建连接
client = pymongo.MongoClient("localhost", 27017)
db = client.test_database
