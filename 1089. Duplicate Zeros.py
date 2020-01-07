class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        N=len(arr)
        ind=0
        add=0
        while ind<N:
            if arr[ind]==0:
                add+=1
                arr.insert(ind,0)
                ind+=2
        for _ in range(add):
            arr.pop()
            


