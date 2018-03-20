# coding=utf-8
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        s=A
        for _ in range(len(A)+1):
            if s==B:
                return True
            s=s[1:]+s[0]
        return False

A = 'abcde'
B = 'cdeab'
A = 'abcde'
B = 'abced'
print(Solution().rotateString(A,B))