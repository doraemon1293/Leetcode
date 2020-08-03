class Solution:
    def maximumSum(self, arr: list) -> int:
        forward_sum = [0] * len(arr)
        ans = forward_sum[0] = arr[0]
        for i in range(1, len(arr)):
            forward_sum[i] = max(arr[i], arr[i] + forward_sum[i - 1])
            ans = max(ans, forward_sum[i])
        backward_sum = [0] * len(arr)
        ans = backward_sum[-1] = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            backward_sum[i] = max(arr[i], arr[i] + backward_sum[i + 1])
            ans = max(ans, backward_sum[i])
        for i in range(1, len(arr) - 1):
            ans = max(ans, forward_sum[i - 1] + backward_sum[i + 1])
        return ans
