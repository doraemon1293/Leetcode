class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':

        a=sum([A[i]*(10**(len(A)-i-1)) for i in range(len(A))])+K
        return [int(x) for x in str(a)]