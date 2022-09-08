from typing import List
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        for q in queries:
            temp=0
            l=0
            for num in nums:
                if temp+num<=q:
                    temp+=num
                    l+=1
                else:
                    break
            ans.append(l)
        return ans

