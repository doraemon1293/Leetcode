class Solution:
    def tribonacci(self, n: int) -> int:
        if n==1:
            return 0
        elif n==2 or n==3:
            return 1
        t0 = 0
        t1 = t2 = 1

        for i in range(3,n):
            t = t1 + t2 + t0
            t0, t1, t2 = t1, t2, t
        return t
