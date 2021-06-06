import collections


class Solution:
    def splitString(self, s: str) -> bool:
        dp = collections.defaultdict(list)
        for i in range(len(s)):
            temp=[]
            for k in dp:
                for number,end in dp[k]:
                    if int(s[k+1:i+1])==end-1:
                        temp.append((number+1,end-1))

            temp.append((1, int(s[:i + 1])))
            dp[i]=temp
        # print(dp)
        return bool([x for x in dp[len(s)-1] if x[0]>=2])