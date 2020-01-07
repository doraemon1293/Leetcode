class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        ans = []
        summ=sum(A)
        for v, i in queries:
            if A[i]%2==0:
                summ-=A[i]
            A[i]+=v
            if A[i]%2==0:
                summ+=A[i]
            ans.append(summ)
        return ans
