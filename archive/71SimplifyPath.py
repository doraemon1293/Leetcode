# coding=utf-8
'''
Created on 2017å¹?6æœ?13æ—?

@author: Administrator
'''


class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = []
        path = path.split("/")
        for x in path:
            if x:
                if x == "..":
                    if s:
                        s.pop()
                elif x != ".":
                    s.append(x)
        return "/" + "/".join(s)


path = "/../"
path = "/home//foo/"
path = "/a/./b/../../c/"
print Solution().simplifyPath(path)
