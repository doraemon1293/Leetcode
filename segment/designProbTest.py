# coding=utf-8
'''
Created on 2017�?8�?10�?

@author: Administrator
'''


def designProbTest(functions, parameters):
    for i in range(len(functions)):
        f, para = functions[i], parameters[i]
        if f[i].isupper():
            cls = eval(f + "(*para)")
        else:
            print(eval("cls." + f + "(*para)"))
