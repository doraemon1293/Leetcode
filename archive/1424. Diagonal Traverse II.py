class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagnals = {}
        max_keys = -1
        ans = []
        for r in range(len(nums) - 1, -1, -1):
            for c in range(len(nums[r])):
                diagnals.setdefault(r + c, [])
                diagnals[r + c].append(nums[r][c])
                max_keys = max(max_keys, r + c)

        for k in range(max_keys + 1):
            ans += diagnals.get(k, [])
        return ans
