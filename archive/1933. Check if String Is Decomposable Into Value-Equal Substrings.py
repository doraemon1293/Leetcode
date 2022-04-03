class Solution:
    def isDecomposable(self, s: str) -> bool:
        c=None
        l=0
        s=s+" "
        s2=0
        for ch in s:
            if ch==c:
                l+=1
            else:
                if l%3==2:
                    if s2==1:
                        return False
                    else:
                        s2=1
                elif l%3==0:
                    pass
                else:
                    return False
                c=ch
                l=1
        return s2==1