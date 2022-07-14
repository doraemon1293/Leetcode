class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        ans=[]
        for q in queries:
            if q>int("9"+"0"*((intLength+1)//2-1)):
                ans.append(-1)
            else:
                s=str(int("1"+"0"*((intLength+1)//2-1))+q-1)
                if intLength%2==0:
                    ans.append(s+s[::-1])
                else:
                    ans.append(s+s[::-1][1:])
        return ans