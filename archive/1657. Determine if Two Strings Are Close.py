import collections
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1,c2=collections.Counter(word1),collections.Counter(word2)
        print(sorted(c1.values()))
        print(sorted(c2.values()))
        print(set(word1))
        if sorted(c1.values())==sorted(c2.values()) and set(word1)==set(word2):
            return True
        else:
            return False