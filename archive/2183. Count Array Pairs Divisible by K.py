from typing import List
import collections
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        def gcd(a,b):
            while a%b:
                a,b=b,a%b
            return b

        d_gcd=collections.defaultdict(int)
        ans=0
        for num in nums:
            g1=gcd(num,k)
            for g2,count in d_gcd.items():
                if g1*g2%k==0:
                    ans+=count
            d_gcd[g1]+=1
        return ans






        not_div_by_k=[num for num in nums if num%k]
        n,m=len(nums),len(not_div_by_k)
        return n*(n-1)//2-m*(m-1)//2


nums=[8,10,2,5,9,6,3,8,2]
k=6
print(Solution().countPairs(nums,k))