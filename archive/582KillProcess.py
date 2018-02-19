# coding=utf-8
'''
Created on 2017å¹?5æœ?14æ—?

@author: Administrator
'''


class Solution(object):

    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        from collections import deque
        ppid_pid = {}
        for i, x in enumerate(ppid):
            ppid_pid.setdefault(x, set())
            ppid_pid[x].add(pid[i])
        ans = []
        if kill in pid:
            q = deque([kill])
        else:
            q = deque()
        while q:
            x = q.popleft()
            ans.append(x)
            q.extend(ppid_pid.get(x, set()))
        return ans


pid = [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
print Solution().killProcess(pid, ppid, kill)

