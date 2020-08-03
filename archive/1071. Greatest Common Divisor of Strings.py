class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for length in range(len(str1),0,-1):
            div1,mod1=divmod(len(str1),length)
            div2,mod2=divmod(len(str2),length)
            if mod1==mod2==0:
                if str1==str1[:length]*div1 and str2==str1[:length]*div2:
                    return str1[:length]
        return ""



