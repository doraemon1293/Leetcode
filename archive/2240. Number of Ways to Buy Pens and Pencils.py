class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans=0
        for pen in range(total//cost1+1):
            if total-pen*cost1>=0:
                pencil=(total-pen*cost1)//cost2
                # print(pen,pencil)
                ans+=pencil+1
        return ans