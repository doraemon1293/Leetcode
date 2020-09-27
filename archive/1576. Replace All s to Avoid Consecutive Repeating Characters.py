class Solution:
    def modifyString(self, s: str) -> str:
        s=list(s)
        i=0
        for i in range(len(s)):
            if s[i]=="?":
                s[i]="a"
                while (i-1>=0 and s[i-1]==s[i]) or (i+1<len(s) and s[i+1]==s[i]):
                    s[i]=chr(ord(s[i])+1)
        return "".join(s)