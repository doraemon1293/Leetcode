# coding=utf-8
'''
Created on 2017å¹?8æœ?10æ—?

@author: Administrator
'''


def designProbTest(functions, parameters):
    for i in xrange(len(functions)):
        f, para = functions[i], parameters[i]
        if f[0].isupper():
            cls = eval(f + "(*para)")
        else:
            print eval("cls." + f + "(*para)")
