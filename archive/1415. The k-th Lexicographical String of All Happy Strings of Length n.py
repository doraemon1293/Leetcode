class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ind = 0
        ans = []

        def dfs(s):
            if len(ans)==k:
                return
            if len(s) == n:
                ans.append(s)
            else:
                for ch in "abc":
                    if s == "" or s[-1] != ch:
                        dfs(s + ch)


        dfs("")
        if len(ans) == k:
            return ans[-1]
        else:
            return ""


n = 3
k = 9
print(Solution().getHappyString(3, 9))
