from typing import List
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefixsum=[0]
        memo={}
        for x in stoneValue:
            prefixsum.append(prefixsum[-1]+x)

        def summ(st,end):
            return prefixsum[end+1]-prefixsum[st]

        def foo(st,end):
            if st==end:
                return 0
            if (st,end) in memo:
                return memo[st,end]
            right_sum=summ(st,end)
            left_sum=0
            res=0
            for i in range(st,end):
                left_sum+=stoneValue[i]
                right_sum-=stoneValue[i]
                if left_sum>right_sum:
                    temp=right_sum+foo(i+1,end)
                    res=max(temp,res)
                elif left_sum<right_sum:
                    temp=left_sum+foo(st,i)
                    res=max(temp,res)
                else:
                    temp1=left_sum+foo(st,i)
                    temp2=right_sum+foo(i+1,end)
                    res=max(res,temp1,temp2)
            memo[st,end]=res
            return res
        return foo(0,len(stoneValue)-1)