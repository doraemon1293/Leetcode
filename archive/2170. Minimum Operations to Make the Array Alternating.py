import collections


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        counter_even = collections.Counter([nums[i] for i in range(0, len(nums), 2)])
        counter_odd = collections.Counter([nums[i] for i in range(1, len(nums), 2)])
        x = counter_even.most_common(2)
        if len(x) == 2:
            x1, x2 = x
        else:
            x1 = x[0]
            x2 = (None, 0)

        y = counter_odd.most_common(2)
        if len(y) == 2:
            y1, y2 = y
        else:
            y1 = y[0]
            y2 = (None, 0)
        if x1[0] != y1[0]:
            return len(nums) - x1[1] - y1[1]
        else:
            return len(nums) - max(x1[1] + y2[1], x2[1] + y1[1])
