from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # prefix=[0]
        # for num in nums:
        #     prefix.append(prefix[-1]+num)

        prefix_set={0}
        prefix_sum=0
        ans=0
        for num in nums:
            prefix_sum+=num
            if prefix_sum-target in prefix_set:
                prefix_set={0}
                prefix_sum=0
                ans+=1
            else:
                prefix_set.add(prefix_sum)
        return ans