#__author__ = 'James'
#-*- coding:utf-8 -*-

#lines生成器只是在文件的最后追加一个空行
#任何包含yield语句的函数称为生成器（P154）
def lines(file):
    for line in file:yield line
    yield '\n'

#收集遇到的所有行，直到遇到一个空行，然后返回已收集的行。之后再次开始收集
#下面的值在作为boolean表达式时会被视为假：False,None,0,"",(),[],{}
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
