class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d={}
        for word in words:
            for ch in word:
                d.setdefault(ch,0)
                d[ch]+=1
        for ch in d:
            if d[ch]%len(words)!=0:
                return False
        return True