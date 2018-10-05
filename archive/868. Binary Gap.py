class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)[2:]
        print(s)
        ans = 0
        last_i = -1
        for i in range(len(s)):
            if s[i] == "1":
                if last_i != -1:
                    ans = max(ans, i - last_i)
                    last_i=i
                else:
                    last_i=i
        return ans



N = 22
print(Solution().binaryGap(N))
