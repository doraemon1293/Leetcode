# coding=utf-8
'''
Created on 2017å¹?8æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ans = set()

        def dfs(s, k, pre):
            if k == 1:
                if s and (not s.startswith("0") or s == "0") and int(s) <= 255:
                    self.ans.add(pre + "." + s)
                return
            n = len(s)
            if n > k * 3 or n < k: return
            dfs(s[1:], k - 1, pre + ("." if pre else "") + s[:1])
            if s[0] != "0": dfs(s[2:], k - 1, pre + ("." if pre else "") + s[:2])
            if s[0] != "0" and int(s[:3]) <= 255: dfs(s[3:], k - 1, pre + ("." if pre else "") + s[:3])

        dfs(s, 4, "")
        return list(self.ans)


s = "255255255255"
print Solution().restoreIpAddresses(s)

