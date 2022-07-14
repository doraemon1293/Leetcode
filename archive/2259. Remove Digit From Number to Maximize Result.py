class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans=""
        for i in ([ind for ind in range(len(number)) if number[ind]==digit]):
            ans=max(ans,number[:i]+number[i+1:])
        return ans
