class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        summ=sum(batteries)
        batteries.sort()
        while batteries[-1]>summ/n:
            x=batteries.pop()
            n-=1
            summ-=x
        return summ/n