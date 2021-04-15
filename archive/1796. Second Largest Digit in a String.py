class Solution:
    def secondHighest(self, s: str) -> int:
        arr=sorted(set([int(ch) for ch in s if ch.isdigit()]),reverse=True)
        return arr[1] if len(arr)>=2 else -1