from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans=[]
        for ch in range(26):
            ch=chr(ord('a')+ch)
            num=float("inf")
            for word in A:
                counter=Counter(word)
                num=min(counter[ch] if ch in counter else 0,num)
            ans+=[ch]*num
        return ans