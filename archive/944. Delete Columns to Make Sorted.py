class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ans = 0
        for col in zip(*A):
            print(col)
            for i in range(len(A) - 1):
                if col[i] > col[i + 1]:
                    ans += 1
                    break
        return ans


A =["rrjk","furt","guzm"]
print(Solution().minDeletionSize(A))
