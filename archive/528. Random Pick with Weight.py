import random,bisect
class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.interval=[0]
        for weight in w:
            self.interval.append(self.interval[-1]+weight)


    def pickIndex(self):
        """
        :rtype: int
        """
        temp=random.randint(0,self.interval[-1]-1)
        res=bisect.bisect_right(self.interval,temp)-1
        return res
