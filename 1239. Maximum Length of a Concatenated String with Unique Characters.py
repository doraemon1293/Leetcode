class Solution:
    def maxLength(self, arr: list) -> int:
        dp = [set()]
        for s in arr:
            if len(s) == len(set(s)):
                s = set(s)
                for s1 in dp[:]:
                    if len(s1 & s) == 0:
                        dp.append(s1 | s)
        return max(len(s) for s in dp)



