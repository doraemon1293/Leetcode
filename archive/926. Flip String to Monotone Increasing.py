class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        ones_on_left = [None] * len(S)
        ones = 0
        for i in range(len(S)):
            ones_on_left[i]=ones
            if S[i] == "1":
                ones += 1
        zeros_on_right = [None] * len(S)
        zeros = 0
        for i in range(len(S) - 1, -1, -1):
            zeros_on_right[i]=zeros
            if S[i] == "0":
                zeros += 1
        ans = float("inf")
        for i in range(len(S)):
            ans = min(ans, ones_on_left[i] + zeros_on_right[i])
        print(ones_on_left)
        print(zeros_on_right)
        return ans
