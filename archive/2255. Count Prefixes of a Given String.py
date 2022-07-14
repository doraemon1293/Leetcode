class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return len([w for w in words if s.startswith(w)])