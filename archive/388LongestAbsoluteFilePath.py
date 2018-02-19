# coding=utf-8
'''
Created on 2017å¹?8æœ?14æ—?

@author: Administrator
'''


class Solution(object):

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        input = input.split("\n")
        dir = {}
        ans = 0
        for line in input:
            if line:
                level = 0
                while line[level] == "\t":
                    level += 1
                dir[level] = line[level:]
                if "." in dir[level]:
                    s = "/".join([dir[i] for i in xrange(level + 1)])
                    ans = max(len(s), ans)
        return ans


input = "dir/subdir2/subsubdir2/file2.ext"
print Solution().lengthLongestPath(input)

