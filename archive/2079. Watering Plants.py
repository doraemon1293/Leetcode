from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        max_capacity = capacity
        for i, p in enumerate(plants):
            if capacity >= p:
                ans += 1
                capacity -= p
            else:
                ans += i
                capacity = max_capacity


                ans += i + 1
                capacity -= p
        return ans
