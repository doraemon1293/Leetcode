import re
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set([int(x) for x in re.split(r"[a-z]+",word) if x!=""]))

print(Solution().numDifferentIntegers("a123bc34d8ef34"))
