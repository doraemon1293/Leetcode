import itertools
class Solution:
    def minimumSum(self, num: int) -> int:
        ans=float("inf")
        for i in range(4):
            num1=int(str(num)[i])
            num2=int(sorted(str(num)[:i]+str(num)[i+1:]))
            ans=min(ans,num1+num2)


        for comb1 in itertools.combinations((0,1,2,3),2):
            comb2={0,1,2,3}-set(comb1)
            num1=int("".join(sorted([num[i] for i in comb1])))
            num2=int("".join(sorted([num[i] for i in comb2])))
            ans=min(ans,num1+num2)
        return ans


