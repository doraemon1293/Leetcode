class Solution:
    def sequentialDigits(self, low: int, high: int) -> list:

        def foo(n):
            number=int("".join([str(i+1) for i in range(n)]))
            res=[]
            while number%10:
                res.append(number)
                number+=int("".join(["1"]*n))
            return res
        res=[]
        for i in range(1,10):
            res+=foo(i)
        ans=[i for i in res if low<=i<=high]
        return ans
print(Solution().sequentialDigits(100,300))