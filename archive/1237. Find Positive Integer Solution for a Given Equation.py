"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        x = 1
        ans = []
        for y in range(1, 1001):
            if customfunction.f(x, y) >= z:
                break
        if customfunction.f(x, y) == z:
            ans.append([x, y])
        for x in range(2, 1001):
            while y > 0 and customfunction.f(x, y) >= z:
                if customfunction.f(x, y) == z:
                    ans.append([x, y])
                y -= 1
        return ans









