# coding=utf-8
'''
Created on 2017�?2�?21�?

@author: Administrator
'''


class Solution(object):

    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        import re
        p = re.compile(r"^(?:(?:[A-Z]+)|(?:[a-z]+)|(?:[A-Z]{1}[a-z]*))$")
        if re.match(p, word):
            return True
        else:
            return False
