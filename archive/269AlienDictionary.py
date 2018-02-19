# coding=utf-8
'''
Created on 2017å¹?10æœ?12æ—?

@author: Administrator
'''


class Solution(object):

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        edges = {}
        indegree = {}
        zeroDegree = set()
        for word in words:
            for ch in word:
                edges.setdefault(ch, set())
                zeroDegree.add(ch)

        for i in range(len(words)):
            s1 = words[i]
            for j in range(i + 1, len(words)):
                s2 = words[j]
                k = 0
                while k < min(len(s1), len(s2)) and s1[k] == s2[k]:
                    k += 1
                if k < min(len(s1), len(s2)):
                    a, b = s1[k], s2[k]
                    if b not in edges[a]:
                        edges[a].add(b)
                        indegree.setdefault(b, 0)
                        indegree[b] += 1
                        zeroDegree.discard(b)
#         print indegree
#         print edges
#         print zeroDegree
        ans = []
        while zeroDegree:
            ch = zeroDegree.pop()
            ans.append(ch)
            for x in edges[ch]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    zeroDegree.add(x)
                    del indegree[x]
#             print indegree
#             print zeroDegree
        if len(indegree):
            return ""
        else:
            return "".join(ans)


words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
words = ["z", "x", "z"]
words = ["l", "wdhfgbdt", "vzd", "qqddytlfd", "jj", "vw", "kkeqazf", "pmc", "eezyjdkmdf", "pe", "aphr", "jhmdv", "gemcj", "q", "ucpnquufb", "jdilhilfn"]
words = ["wrt", "wrtkj"]
print Solution().alienOrder(words)

