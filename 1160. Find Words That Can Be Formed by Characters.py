import collections
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter_chars=collections.Counter(chars)
        ans=0
        for word in words:
            counter=collections.Counter(word)
            flag=True
            for ch in counter:
                if counter[ch]>counter_chars.get(ch,0):
                    flag=False
                    break
            if flag:
                ans+=len(word)
        return ans
