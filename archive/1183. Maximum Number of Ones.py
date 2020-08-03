import math


class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        arr = []
        for x in range(sideLength):
            for y in range(sideLength):
                a = math.ceil((height - x % sideLength) / sideLength)
                b = math.ceil((width - y % sideLength) / sideLength)
                count = a * b
                arr.append(count)
        arr.sort(reverse=1)
        # print(arr)
        return sum(arr[:maxOnes])


width = 3
height = 3
sideLength = 2
maxOnes = 1
print(Solution().maximumNumberOfOnes(width, height, sideLength, maxOnes))
