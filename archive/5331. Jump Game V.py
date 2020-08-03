class Solution:
    def maxJumps(self, arr: list, d: int) -> int:
        mini = min(arr)
        memo = {}

        def foo(ind):
            if arr[ind] == mini:
                return 1
            if ind in memo:
                return memo[ind]
            res = 1
            left = ind - 1
            while left >= 0 and left >= ind - d and arr[left] < arr[ind]:
                res = max(res, foo(left) + 1)
                left -= 1
            right = ind + 1
            while right < len(arr) and right <= ind + d and arr[right] < arr[ind]:
                res = max(res, foo(right) + 1)
                right += 1
            memo[ind] = res
            return res

        return max(foo(ind) for ind in range(len(arr)))


arr = [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12]
d = 2
print(Solution().maxJumps(arr, d))
