#__author__ = 'James'
#-*-coding:utf-8-*-

import sys

punctuations=[',', '.', '?', '!', ':', '[', ']', '(', ')', ';', '\'', '\n']
prepositions=['is','are','am','it', 'an','in','on','with','by','for','at','about','under','of','into','within','throughout','inside','outside','without','from','among',
              'the','this','that','which','if','and','each','where','every','one','any','was','to','or','you','he','she','we','they']

def words_statistics(file_path):
    file = open(file_path, 'r')
    str = file.read()

    for i in punctuations:
        str = str.replace(i, ' ')

    list = str.strip().split(' ')
    dic = {}
    for item in list:
        if item and len(item)>1 :
            if item.lower() in prepositions :continue
            else: dic[item]=1
    for item in list:
        if item and len(item)>1 :
            if item.lower() in prepositions :continue
            else:  dic[item]+=1
    result = sorted(dic.items(), lambda x,y: cmp(x[1], y[1]), reverse=True)

    return result

if __name__=='__main__':
    filelist = sys.argv[1:]
    for file in filelist:
        print u'文件'+str(file)+u'单词统计:'
        print words_statistics(file)