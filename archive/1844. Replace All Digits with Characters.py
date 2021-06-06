class Solution:
    def replaceDigits(self, s: str) -> str:
        ans=[]
        for i in range(len(s)):
            if s[i].isalpha():
                ch=s[i]
                ans.append(ch)
            else:
                ch=chr(ord(ch)+int(s[i]))
                ans.append(ch)
        return "".join(ans)