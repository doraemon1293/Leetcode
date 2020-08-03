class Solution:
    def kConcatenationMaxSum(self, arr: list, k: int) -> int:

        temp = 0
        max_sub_arr_sum = 0
        mini = 0
        presum = [0] * len(arr)
        for i, a in enumerate(arr):
            temp += a
            presum[i] = temp
            max_sub_arr_sum = max(max_sub_arr_sum, temp - mini)
            mini = min(mini, temp)
        susum = [0] * len(arr)
        temp = 0
        for i in range(len(arr) - 1, -1, -1):
            temp += arr[i]
            susum[i] = temp
        return max(max(presum + [0]) + max(susum + [0]) + (k - 2) * sum(arr), max_sub_arr_sum, max(presum + [0]) + max(susum + [0])) % (10 ** 9 + 7)


arr = [-9, 13, 4, -16, -12, -16, 3, -7, 5, -16, 16, 8, -1, -13, 15, 3]
k = 6
print(Solution().kConcatenationMaxSum(arr, k))
