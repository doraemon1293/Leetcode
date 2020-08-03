class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}

        def dp(st,summ):
            if st in memo:
                return memo[st]
            if st==len(stoneValue):
                return 0
            if st==len(stoneValue)-1
                return stoneValue[st]
            temp=stoneValue[st]
            r1 = temp + (summ - temp - dp(st+1, summ - temp))
            if st<=len(stoneValue)-2:
                temp+=stoneValue[st+1]
                r2 = temp + (summ - temp - dp(st+2, summ - temp))
            else:
                r2 = -float("inf")
            if st<=len(stoneValue)-3:
                temp += stoneValue[st + 2]
                r3 = temp + (summ - temp - dp(st+3, summ - temp))
            else:
                r3 = -float("inf")
            res = max(r1, r2, r3)
            memo[st] = res
            return res

        summ = sum(stoneValue)
        a = dp(0, summ)
        b = summ - a
        if a > b:
            return "Alice"
        if a < b:
            return "Bob"
        if a == b:
            return "Tie"


