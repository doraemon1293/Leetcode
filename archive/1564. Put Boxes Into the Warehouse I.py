from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        mini = float("inf")
        heights = []
        for h in warehouse:
            mini = min(mini, h)
            heights.append(mini)
        ans = 0
        n = len(boxes)
        boxes.sort(reverse=True)
        for h in heights[::-1]:

            if boxes and h >= boxes[-1]:
                boxes.pop()
        return n - len(boxes)





