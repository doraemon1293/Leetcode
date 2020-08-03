class Solution:
    def removeVowels(self, S: str) -> str:
        return  "".join([ch for ch in S if ch not in ("a","e","i","o","u")])