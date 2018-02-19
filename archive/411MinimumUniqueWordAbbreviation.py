# coding=utf-8
'''
Created on 2017�?9�?29�?

@author: Administrator
'''


class Solution(object):

    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """

        def toNumbers(target, dictionary):
            numbers = []
            for word in dictionary:
                if len(word) == len(target):
                    number = 0
                    for i in range(len(word)):
                        number <<= 1
                        number += word[i] != target[i]
                    numbers.append(number)
            return numbers

        def ithDigit(number, i):
            return (number >> len(target) - i - 1) & 1

        def numberToWord(number):
            count = 0
            res = ""
            for i in range(len(target)):
                if ithDigit(number, i):
                    if count != 0:
                        res += str(count)
                    res += target[i]
                    count = 0
                else:
                    count += 1
            if count != 0:
                res += str(count)
            return res

        def isValid(number, numbers):
            return all([number & x != 0 for x in numbers])

        def dfs(number, depth, length):
            if length >= self.min_length:
                return
            if depth == len(target):
                if isValid(number, numbers):
                    self.min_length = length
                    self.ans = number
                return
            # 设置第depth位是0
            if length == 0:
                new_length = 1
            else:
                new_length = length + 1 if ithDigit(number, depth - 1) else length
            dfs(number, depth + 1, new_length)
            # 设置第depth位是1
            if depth not in zeros:
                new_number = number | (1 << (len(target) - depth - 1))
                new_length = length + 1
                dfs(new_number, depth + 1, new_length)

        self.min_length = len(target)
        self.ans = (1 << len(target)) - 1
        numbers = toNumbers(target, dictionary)
        zeros = set([i for i in range(len(target)) if all([ithDigit(number, i) == 0 for number in numbers])])
        dfs(0, 0, 0)
        return numberToWord(self.ans)


target = "apple"
dictionary = ["kkkk"]
target = "abc"
dictionary = ["abd", "acd", "acc"]
print Solution().minAbbreviation(target, dictionary)

