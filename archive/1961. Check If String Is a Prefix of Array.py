class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for w in words:
            if s.startswith(w):
                s=s[len(w):]
                if s=="":
                    return True
            else:
                return False
        return s==""