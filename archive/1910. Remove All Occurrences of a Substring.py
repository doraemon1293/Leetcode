class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ans = ""
        for ch in s:
            ans += ch
            if len(ans) >= len(part) and ans[-len(part):] == part:
                ans = ans[:-len(part)]
        return ans
