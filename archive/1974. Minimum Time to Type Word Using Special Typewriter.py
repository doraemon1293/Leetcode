class Solution:
    def minTimeToType(self, word: str) -> int:
        pointing='a'
        ans=0
        for ch in word:
            move=min(abs(ord(ch)-ord(pointing)),26-abs(ord(ch)-ord(pointing)))
            ans+=move+1
            pointing=ch
        return ans
