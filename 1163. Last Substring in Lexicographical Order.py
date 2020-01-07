class Solution:
    def lastSubstring(self, s: str) -> str:
        if len(set(str))==1:
            return str
        max_char = chr(96)
        candidates = []
        for i, ch in enumerate(s):
            if ch > max_char:
                candidates = [i]
                max_char = ch
            elif ch == max_char:
                candidates.append(i)
        ans = [max_char]
        while candidates:
            next_chars = set([s[i + 1] for i in candidates if i+1<len(s)])
            if next_chars:
                max_char=max(next_chars)
                ans.append(max_char)
                candidates=[i+1 for i in candidates if i+1<len(s) and s[i+1]==max_char]
            else:
                candidates=[]
        return "".join(ans)

s="abab"
print(Solution().lastSubstring(s))
