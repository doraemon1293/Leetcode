import bisect


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k==1:
            return 1

        fibs = [1, 2]
        while fibs[-1]+fibs[-2] <= k:
            fibs.append(fibs[-1] + fibs[-2])
        ans = 0
        while k:
            k = k - fibs[-1]
            x = bisect.bisect_right(fibs, k)
            fibs = fibs[:x]
            ans += 1
        return ans


k=999999
k=5
print(Solution().findMinFibonacciNumbers(k))