class Solution:
    def toHexspeak(self, num: str) -> str:
        num=int(num)
        h=[]
        while num:
            h.append(num%16)
            num=num//16
        for i,x in enumerate(h):
            if x==0:
                h[i]="O"
            elif x==1:
                h[i]='I'
            elif x >=10:
                h[i]=chr(ord('A')+(x-10))
            else:
                h=None
                break
        if h!=None:
            return "".join(h[::-1])
        else:
            return "ERROE"
