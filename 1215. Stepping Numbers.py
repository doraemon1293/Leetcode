import bisect
class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        total=[0]
        cur=[0]
        while cur:
            new=[]
            for x in cur:
                if x%10!=9:
                    temp=x*10+(x%10+1)
                    if temp<=high:
                        new.append(x)
                if x%10!=0:
                    temp=x*10+(x%10-1)
                    if temp<=high:
                        new.append(x)
            cur=new
            total+=cur
        total.sort()
        return total[bisect.bisect_(total,low):]


