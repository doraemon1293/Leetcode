from typing import  List
import collections
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            while ans and nums[i]<ans[-1] and (len(ans)+(len(nums)-i-1))>=k:
                ans.pop()
            # print(ans)
            ans.append(nums[i])
        return list(ans[:k])
