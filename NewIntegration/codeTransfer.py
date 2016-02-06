#__author__ = 'James'
#-*- coding:utf-8 -*-

def mysterious(ust):                  #定义一个将十六进制代码转换为所代表的字符
       s=""                               #定义一个空字符串
       result = ''
       for i in range(len(ust)/4):        #因为Unicode是4个字符表示一个汉字，每四个一组  #in range 含头不含尾
           us=ust[i*4:i*4+4]              #取的是四位连续的数字，将列表元素赋给字符串
           s=s+unichr(int(us,16))         #将字符串按照十六进制转换为整形数字，
           # print s                        #打印汉字
       return s

def filtrateAndTrans(str):           #将16进制字符串转换为汉字
    print str
    result = ''
    resultList = []
    for str1 in str.split('\u'):
        if str1!='': resultList.append(mysterious(str1))
    # print result.join(resultList)
    return result.join(resultList)

# str='\u4e92\u8054\u7f51\u5927\u4f1a\u6210\u679c\uff1a\u4e60\u8fd1\u5e73\u9610\u8ff0\u4e2d\u56fd\u4e3b\u5f20'
# filtrateAndTrans(str)

