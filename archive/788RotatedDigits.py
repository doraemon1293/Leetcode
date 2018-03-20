class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        d={"0":"0",
           "1": "1",
           "8": "8",
           "2": "5",
           "5": "2",
           "6": "9",
           "9": "6",
           }
        ans=0
        for i in range(1,N+1):
            s=list(str(i))
            flag=True
            for j in range(len(s)):
                if s[j] in d:
                    s[j]=d[s[j]]
                else:
                    flag=False
                    break
            if flag and int("".join(s))!=i:
                ans+=1
        return ans

