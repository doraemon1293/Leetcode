class Solution:
    def countTriples(self, n: int) -> int:
        ans=0
        for a in range(1,n+1):
            for b in range(1,n+1):
                c=a**2+b**2
                if c>n**2:
                    break
                if int(c**0.5)**2==int(c):
                    ans+=1
        return ans