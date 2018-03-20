class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        candidates=[str(i)*2 for i in range(10)]+[chr(ord("a")+i)*2 for i in range(6)]
        ans="#"
        for i in range(3):
            ans+=min([candidate for candidate in candidates],key=lambda x:abs(int(x,16)-int(color[1+i*2:1+i*2+2],16)))
        return ans
color= "#09f166"

print(Solution().similarRGB(color))