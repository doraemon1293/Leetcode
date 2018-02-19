# coding=utf-8
'''
Created on 2017å¹?7æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        ans = [0] * n
        for log in logs:
            f_id, status, timeStamp = log.split(":")
            f_id = int(f_id)
            timeStamp = int(timeStamp)
            if status == "start":
                if stack:
                    f_id1, startTimeStamp = stack[-1]
                    ans[f_id1] += timeStamp - startTimeStamp
                stack.append([f_id, timeStamp])
            else:
                f_id, startTimeStamp = stack.pop()
                ans[f_id] += timeStamp - startTimeStamp + 1
                if stack:
                    stack[-1][1] = timeStamp + 1
        return ans


n = 2
logs = ["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
print Solution().exclusiveTime(n, logs)

