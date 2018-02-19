class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = [None] * len(height)
        max_left = 0
        for i in xrange(len(height)):
            max_left = max(max_left, (height[i - 1] if i - 1 >= 0 else 0))
            left[i] = max_left

        right = [None] * len(height)
        max_right = 0
        for i in xrange(len(height) - 1, -1, -1):
            max_right = max(max_right, (height[i + 1] if i + 1 < len(height) else 0))
            right[i] = max_right

        ans = 0
        for i in xrange(len(height)):
            ans += max(min(left[i], right[i]) - height[i], 0)
        return ans
