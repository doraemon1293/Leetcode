class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words=text.split(" ")
        brokenLetters=set(brokenLetters)
        ans=len(words)
        for w in words:
            for ch in w:
                if ch in brokenLetters:
                    ans-=1
                    break
        return ans