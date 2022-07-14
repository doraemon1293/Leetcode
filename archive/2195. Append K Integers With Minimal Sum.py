class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [0] + sorted(set(nums))
        # print(nums)
        ans = 0
        p = 0
        while k and p < len(nums) - 1:
            a, b = nums[p], nums[p + 1]
            if (b - 1) - (a + 1) + 1 <= k:
                k -= (b - 1) - (a + 1) + 1
                ans += ((a + 1) + (b - 1)) * ((b - 1) - (a + 1) + 1) // 2
            else:
                ans += ((a + 1) + (a + k)) * ((a + k) - (a + 1) + 1) // 2
                k = 0

            p += 1
            # print(a, b, k, ans, p)

        if k:
            ans += ((nums[-1] + 1) + (nums[-1] + k)) * k // 2
        return ans


nums = [17, 18, 19, 19, 21, 22, 25, 29, 32, 33, 35, 40, 44, 47, 50, 52, 60, 61, 72, 84, 84, 86, 88, 94, 96, 98, 99, 100]

k = 35
print(Solution().minimalKSum(nums, k))
