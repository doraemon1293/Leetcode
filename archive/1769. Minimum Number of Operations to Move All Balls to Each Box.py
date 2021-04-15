from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls=[i for i,ch in enumerate(boxes) if ch=="1"]
        ans=[]
        for i in range(len(boxes)):
            ans.append(sum([abs(i-j) for j in balls]))
        return ans

