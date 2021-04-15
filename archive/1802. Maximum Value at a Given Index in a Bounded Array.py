import functools
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        left=index+1
        right=n-index-1

        @functools.lru_cache(None)
        def foo(ni):
            if ni==1:
                return n
            if ni>=left:
                left_sum=(ni+(ni-left+1))*left//2
            else:
                left_sum=(1+ni)*ni//2+(left-ni)
            if ni-1>=right:
                right_sum=(ni-1+(ni-1-right+1))*right//2
            else:
                right_sum=(1+ni-1)*(ni-1)//2+right-(ni-1)
            # print(ni,left_sum+right_sum)
            return left_sum+right_sum
        low,high=1,maxSum
        while low<=high:
            # print(low,high)
            mid=(low+high)//2
            if foo(mid)>maxSum:
                high=mid-1
            elif foo(mid)<maxSum:
                low=mid+1
            else:
                return mid
        return high

print(Solution().maxValue(4,2,6))
print(Solution().maxValue(3,
0,
815094800))
print(Solution().maxValue(9,
6,
27))