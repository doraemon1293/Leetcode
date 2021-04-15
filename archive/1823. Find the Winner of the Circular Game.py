class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=list(range(n))
        ind=0
        while len(arr)>1:
            ind=(ind+k-1)%len(arr)
            del arr[ind]
        return arr[0]+1