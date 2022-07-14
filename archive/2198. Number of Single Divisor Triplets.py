import collections


class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        nums = sorted(set(nums))
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    a, b, c = nums[i], nums[j], nums[k]
                    if sum([(a + b + c) % x == 0 for x in (a, b, c)]) == 1:
                        if a == b and b != c or a == c and b != a:
                            ans += counter[a] * (counter[a] - 1) // 2 * counter[b] * 6
                        elif b == c and b != a:
                            ans += counter[b] * (counter[b] - 1) // 2 * counter[a] * 6
                        else:
                            ans += counter[a] * counter[b] * counter[c] * 6

        return ans
