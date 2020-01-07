class Solution:
    def divisorGame(self, N: int) -> bool:
        d={}
        d[2]=True
        d[1]=False
        def foo(N):
            if N in d:
                return d[N]
            for i in range(1,N):
                if N%i==0:
                    if not foo(N-i):
                        d[N]=True
                        return True
            d[N]=False
            return False
        return foo(N)