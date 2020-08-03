class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        N=len(A)
        for i in range(N-1,-1,-1):
            max_j=-float("inf")
            max_j_ind=None
            for j in range(i+1,N):
                if A[j]<A[i] and max_j<A[j]:
                    max_j=A[j]
                    max_j_ind=j
            if max_j_ind!=None:
                A[i],A[max_j_ind]=A[max_j_ind],A[i]
                return A
        return A

