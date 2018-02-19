class Solution(object):

    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tree = [[None] * 16 for _ in xrange(5)]
        for num in nums:
            d = num / 100 - 1
            p = num % 100 / 10 - 1
            v = num % 10
            tree[d][p] = v
        for x in tree:
            print x
        ans = 0
        for d in xrange(4):
            for p in xrange(16):
                if tree[d][p] != None:
                    l_c = p * 2
                    r_c = p * 2 + 1
                    if tree[d + 1][l_c] == tree[d + 1][r_c] == None:
                        ans += tree[d][p]
                    else:
                        if tree[d + 1][l_c] != None:
                            tree[d + 1][l_c] += tree[d][p]
                        if tree[d + 1][r_c] != None:
                            tree[d + 1][r_c] += tree[d][p]
        return ans


nums = [113, 215, 221]
nums = [111, 217, 221, 315, 415]
print Solution().pathSum(nums)

