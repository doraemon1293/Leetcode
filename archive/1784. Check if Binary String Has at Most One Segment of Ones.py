class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        last="0"
        count=0
        for ch in s:
            if ch=="1":
                if last=="1":
                    pass
                else:
                    last=ch
                    count+=1
            else:
                last=ch
        return count==1

