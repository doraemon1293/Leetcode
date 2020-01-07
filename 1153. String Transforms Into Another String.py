class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        d = {}
        for a, b in zip(str1, str2):
            if d.setdefault(a, b) != b:
                return False
        return len(set(str1)) < 26
