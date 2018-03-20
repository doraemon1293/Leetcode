# coding=utf-8
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        if poured==0:
            return 0
        row=[poured]
        for i in range(1,query_row+1):
            new_row=[0]*(i+1)
            for j in range(len(row)):
                excess=max(row[j]-1,0)
                new_row[j]+=excess/2
                new_row[j+1]+=excess/2
            row=new_row
        print(row)
        return min(row[query_glass],1)



poured = 6
query_row = 2
query_glass = 0
print(Solution().champagneTower(poured, query_row, query_glass))