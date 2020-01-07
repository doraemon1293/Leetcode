class Solution:
    def expand(self, S: str) -> list:
        chars = []
        bracket = False
        temp = []
        for ch in S:
            if ch == "{":
                bracket = True
                temp = []
            elif ch == "}":
                chars.append(temp)
                bracket = False
            elif ch!=",":
                if bracket:
                    temp.append(ch)
                else:
                    chars.append([ch])
        print(chars)
        ans = [""]
        for arr in chars:
            ans=[s+ch for s in ans for ch in arr]
            print(ans)
        ans.sort()
        return ans
S="{a,b}c{d,e}f"

print(Solution().expand(S))