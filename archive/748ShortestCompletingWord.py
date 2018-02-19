# coding=utf-8
'''
Created on 18 Dec 2017

@author: Administrator
'''


class Solution(object):

    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        from collections import Counter
        licensePlate = [ch.lower() for ch in licensePlate if "a" <= ch.lower() <= "z"]
        tcouter = Counter(licensePlate)
        minLength = float("inf")
        for word in words:
            length = len(word)
            temp = [ch.lower() for ch in word if ch.lower() in licensePlate]
            scounter = Counter(temp)
            flag = True
            for ch in tcouter:
                if tcouter[ch] > scounter.get(ch, 0):
                    flag = False
            if flag and length < minLength:
                minLength = length
                ans = word
        return ans

