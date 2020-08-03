class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d=dict([(ch,i) for i,ch in enumerate(keyboard)])
        ans=0
        i=0
        for ch in word:
            j=d[ch]
            ans+=abs(i-j)
            i=j
        return ans