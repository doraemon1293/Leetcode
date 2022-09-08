
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d={}
        ans=0
        for w in words:
            r_w=w[::-1]
            if r_w in d:
                ans+=4
                d[r_w]-=1
                if d[r_w]==0:
                    del d[r_w]
            else:
                d[w]+=1

        for i in range(26):
            if chr(ord("a")+i)*2 in d:
                ans+=1
                break
        return ans
