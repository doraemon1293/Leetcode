# coding=utf-8
'''
Created on 2017å¹?6æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        import re
        p = r"(.*)(\(.*\))"
        d = {}
        for s in paths:
            arr = s.split(" ")
            path = arr[0]
            for ss in arr[1:]:
                m = re.match(p, ss)
                name, content = m.group(1), m.group(2)
                d.setdefault(content, [])
                d[content].append(path + "/" + name)
        # print d
        ans = []
        for v in d.values():
            if len(v) > 1:
                ans.append(v)
        return ans


paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
print Solution().findDuplicate(paths)
