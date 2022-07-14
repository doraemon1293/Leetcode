class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans=0
        num=str(num)
        for i in range(len(num)-k+1):
            print(num[i:i+k])
            if int(num[i:i+k]) and int(num)%int(num[i:i+k])==0:
                    ans+=1
        return ans
