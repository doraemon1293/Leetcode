# coding=utf-8
'''
Created on 2016å¹?11æœ?7æ—?

@author: Administrator
'''


class Solution(object):

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        ransomNote_counter = Counter(ransomNote)
        magazine_couter = Counter(magazine)
        magazine_couter.subtract(ransomNote_counter)
        for x in magazine_couter.values():
            if x < 0:
                return False
        return True


print Solution().canConstruct("a", "b")
1
