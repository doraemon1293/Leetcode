class Solution:
    def largestMultipleOfThree(self, digits: list) -> str:
        bawuer = []
        yisiqi = []
        ans = []
        for digit in digits:
            if digit in (0, 3, 6, 9):
                ans.append(digit)
            if digit in (2, 5, 8):
                bawuer.append(digit)
            if digit in (1, 4, 7):
                yisiqi.append(digit)
        bawuer.sort()
        yisiqi.sort()
        if len(bawuer) % 3 == len(yisiqi) % 3:
            ans += bawuer
            ans += yisiqi
        elif abs(len(bawuer) % 3-len(yisiqi) % 3)==1:
            if len(bawuer)%3>len(yisiqi) % 3:
                ans+=yisiqi
                ans += bawuer[1:]
            if len(bawuer)%3<len(yisiqi) % 3:
                ans+=bawuer
                ans += yisiqi[1:]

        elif abs(len(bawuer) % 3-len(yisiqi) % 3)==2:
            if len(bawuer)%3<len(yisiqi) % 3:
                if len(bawuer) >= 3:
                    ans += bawuer[1:]
                    ans+=yisiqi
                else:
                    ans += bawuer
                    ans += yisiqi[2:]
            if len(bawuer)%3>len(yisiqi) % 3:
                if len(yisiqi) >= 3:
                    ans += yisiqi[1:]
                    ans+=bawuer
                else:
                    ans += yisiqi
                    ans += bawuer[2:]
        ans.sort(reverse=True)
        if len(ans) == 0:
            return ""
        p = 0
        while p < len(ans) and ans[0] == 0:
            p += 1
        if p == len(ans):
            return "0"
        return "".join(str(x) for x in ans[p:])

digits = [5, 8]
digits=[0,0,0]
# digits = [8, 6, 7, 1, 0]
# digits=[1,1,1,2]
# digits=[1,1,1]
# digits = [2, 2, 1, 1, 1]

print(Solution().largestMultipleOfThree(digits))
