class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)!=len(B):
            return False
        if A==B:
            if len(set(A))!=len(A):
                return True
        N=len(A)
        arr=[]
        for i in range(N):
            if A[i]!=B[i]:
                if len(arr)>=2:
                    return False
                arr.append(i)
        if len(arr)==2 and A[arr[0]]==B[arr[1]] and A[arr[1]]==B[arr[0]]:
            return True
        else:
            return False
