class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:

        s1=sorted(s1)
        s2=sorted(s2)
        return all([a>=b for a,b in zip(s1,s2)]) or all([b>=a for a,b in zip(s1,s2)])
