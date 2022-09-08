class Solution(object):
    def countTexts(self, pressedKeys):
        """
        :type pressedKeys: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp = [1]
        for i in range(len(pressedKeys)):
            ch = pressedKeys[i]
            res = dp[i]
            l = 3 if ch not in ("7","9") else 4
            for j in range(1, l):
                if i - j >= 0 and ch == pressedKeys[i - j]:
                    res = (res + dp[i - j]) % MOD
                else:
                    break

            dp.append(res)
        # print(dp)
        return dp[-1]