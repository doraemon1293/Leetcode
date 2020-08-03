from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        last_op=0
        ans=0
        for x in target:
            if x > last_op:
                ans+=x-last_op
                last_op=x
            else:
                last_op=x
        return ans
s=open("../input", "r").readline()
target=eval(s)
print(Solution().minNumberOperations(target))