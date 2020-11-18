class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_no=[0]
        for i in range(len(s)):
            if s[i]=="b":
                b_no.append(b_no[-1]+1)
            else:
                b_no.append(b_no[-1])
        ans=float("inf")
        for i in range(len(s)+1):
            ans=min(ans,b_no[i]+(len(s)-i-(b_no[-1]-b_no[i])))
        return ans



s="ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa"
s="aababbab"
s="a"
print(Solution().minimumDeletions(s))