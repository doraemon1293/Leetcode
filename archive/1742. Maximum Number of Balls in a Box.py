import collections


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ans=collections.Counter([sum([int(ch) for ch in str(i)]) for i in range(lowLimit, highLimit + 1)])
        # print(ans)
        return ans.most_common(1)[0][1]

print(Solution().countBalls(1,10))