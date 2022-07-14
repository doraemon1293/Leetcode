class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        ans = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                ans = max(ans, num[i:i + 3])
        return ans
