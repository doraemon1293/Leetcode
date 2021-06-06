class Solution:
    def minSwaps(self, s: str) -> int:
        zeros=ones=0
        for ch in s:
            if ch=="1":
                ones+=1
            else:
                zeros+=1
        if abs(zeros-ones)>=2:
            return -1
        if len(s)%2:
            ans=0
            if ones>zeros:
                first="1"
            else:
                first="0"
            for ch in s:
                if ch!=first:
                    ans+=1
                first="1" if first=="0" else "0"
            return ans//2
        else:
            ans=len(s)
            for first in ("0","1"):
                temp = 0
                for ch in s:
                    if ch != first:
                        temp += 1
                    first = "1" if first == "0" else "0"
                ans=min(ans,temp//2)
            return ans

