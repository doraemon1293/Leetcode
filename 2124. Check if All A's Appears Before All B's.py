class Solution:
    def checkString(self, s: str) -> bool:
        ia=-1
        ib=len(s)
        for i,ch in enumerate(s):
            if ch=="a":
                ia=i
            else:
                ib=min(ib,i)
        return ia>ib

