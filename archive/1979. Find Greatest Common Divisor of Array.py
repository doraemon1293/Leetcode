class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            while a%b:
                a,b=b,a%b
            return b

        g=nums[0]
        for i in range(len(nums)-1):
            g=gcd(nums[i+1],g)
            if g==1:
                return 1
        return g