class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        summ=sum(A)
        if summ%3:
            return False
        target=summ//3
        p1=p2=0
        cur_sum1=0
        N=len(A)
        for p1 in range(N):
            cur_sum1+=A[p1]
            if cur_sum1==target:
                cur_sum2=0
                for p2 in range(p1+1,N):
                    cur_sum2+=A[p2]
                    if cur_sum2==target:
                        return True
        return False





