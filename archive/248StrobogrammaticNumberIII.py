# coding=utf-8
'''
Created on 2017å¹?10æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        if int(low) > int(high): return 0
        self.memo = {0:[], 1:["0", "1", "8"], 2:["11", "69", "88", "96"]}

        def findStrobogrammaticWithLengthN(n):
            """
            :type n: int
            :rtype: List[str]
            """
            if n in self.memo:
                return self.memo[n]
            arr1 = ["0", "1", "8"]
            arr2 = ["00", "11", "69", "88", "96"]
            if n % 2 == 1:
                res = [x[:len(x) / 2] + y + x[len(x) / 2:] for x in findStrobogrammaticWithLengthN(n - 1) for y in arr1]
            else:
                res = [x[:len(x) / 2] + y + x[len(x) / 2:] for x in findStrobogrammaticWithLengthN(n - 2) for y in arr2]
            self.memo[n] = res
            return res

        for i in xrange(len(high) + 1, -1, -1):
            findStrobogrammaticWithLengthN(i)
        ans = 0
        for i in xrange(len(low) + 1, len(high)):
            ans += len(self.memo[i])
        if len(high) == len(low):
            ans += len([num for num in self.memo[len(high)] if int(low) <= int(num) <= int(high)])
        else:
            ans += len([num for num in self.memo[len(high)] if int(num) <= int(high)])
            ans += len([num for num in self.memo[len(low)] if int(num) >= int(low)])
        return ans


low = "100"
high = "1000"
print Solution().strobogrammaticInRange(low, high)
