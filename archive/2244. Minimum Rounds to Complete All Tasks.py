import collections
import math
class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        c=collections.Counter(tasks)
        ans=0
        for v in c.values():
            if v==1:
                return -1

            ans+=math.ceil(v/3)
        return ans
