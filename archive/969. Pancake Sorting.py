class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        ans=[]
        for a in range(N,0,-1):
            #1 put a in the front of A
            ind=A.index(a)
            ans.append(ind+1)
            A[:ind+1]=A[:ind+1][::-1]
            #2 put a in place
            ans.append(a)
            A[:a]=A[:a][::-1]

        return ans

