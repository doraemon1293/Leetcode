class Solution:
    def isThree(self, n: int) -> bool:

        if n==1:
            return False
        if int(n**0.5)**2==n:
            x=int(n**0.5)
            for i in range(2,x):
                if x%i==0:
                    return False
            return True
        else:
            return False