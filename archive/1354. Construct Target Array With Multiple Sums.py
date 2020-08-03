class Solution:
    def isPossible(self, target: list) -> bool:
        while True:
            target.sort()
            maxi = target[-1]
            if maxi == 1:
                return True
            summ = sum(target)
            if maxi-(summ-maxi) <= 0:
                return False
            target[-1] =maxi-(summ-maxi)


target=[9,3,5]
print(Solution().isPossible(target))