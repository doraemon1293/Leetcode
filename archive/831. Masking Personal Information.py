class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        def mask_email(S):
            name1,other=S.split("@")
            name1=name1.lower()[0]+"*****"+name1.lower()[-1]
            return name1+"@"+other.lower()
        def mask_phone(S):
            S="".join(filter(lambda x:x.isdigit(),S))
            if len(S)==10:
                return "***-***-"+S[-4:]
            else:
                return "+{}-".format("*"*(len(S)-10))+"***-***-"+S[-4:]

        if "@" in S:
            return  mask_email(S)
        else:
            return mask_phone(S)
S="860-(10)12345678"
#S="1(234)567-890"
print(Solution().maskPII(S))