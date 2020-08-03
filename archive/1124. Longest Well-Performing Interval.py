class Solution:
    def longestWPI(self, hours: list) -> int:
        presum=[0]
        for hour in hours:
            if hour>8:
                presum.append(presum[-1]+1)
            else:
                presum.append(presum[-1]-1)
        print(presum)
        stack=[]
        for i,x in enumerate(presum):
            if len(stack)==0 or x<stack[-1][1]:
                stack.append((i,x))
        print(stack)
        ans=0
        for j in range(len(presum)-1,-1,-1):
            while stack and stack[-1][1]<presum[j]:
                i=stack.pop()[0]
                ans=max(ans,j-i)
        return ans
hours=[9,9,6,0,6,6,9]

print(Solution().longestWPI(hours))