from typing import List
import math


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minute = [math.ceil(a / b) for a, b in zip(dist, speed)]
        minute.sort()
        # print(minute)
        for i in range(len(minute)):
            if minute[i] <= i:
                return i
        return len(minute)
