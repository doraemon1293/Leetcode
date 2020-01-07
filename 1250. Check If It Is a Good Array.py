class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        gcd = A[0]
        for a in nums:
            while a:
                gcd, a = a, gcd % a
        return gcd == 1
