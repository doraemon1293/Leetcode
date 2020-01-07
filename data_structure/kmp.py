# coding=utf-8
'''
Created on 2017�?7�?6�?

@author: Administrator
'''


def get_next(p):
    next = [0] * len(p)
    for ind in range(1, len(p)):
        k = next[ind - 1]
        if p[ind] == p[k]:
            next[ind] = k + 1
        else:
            while k:
                k = next[k - 1]
                if p[k] == p[ind]:
                    next[ind] = k + 1
                    break
    return next


def kmp_match(s, p):
    m = len(s)
    n = len(p)
    cur = 0  # 起始指针cur
    next = get_next(p)
    while cur <= m - n:
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - next[i - 1], 1)  # 有了部分匹配�?,我们不只是单纯的1�?1位往右移,可以�?次移动多�?
                break
        else:
            return cur  #for 循环中，如果没有从任何一个 break 中退出，则会执行和 for 对应的 else
                        #只要从 break 中退出了，则 else 部分不执行。
    return False


print(kmp_match("ABCDAB ABCDABCDABDE", "ABCDABD"))
print(get_next("ABCDABD"))
s = "acaa"
print(s + "#" + s[::-1])
print(get_next(s + "#" + s[::-1]))

print(get_next("0000000100"))
print(kmp_match("0000001000", "0000000100"))

print(get_next("abcddcba"))

