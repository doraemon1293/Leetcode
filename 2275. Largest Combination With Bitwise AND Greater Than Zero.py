class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        arr=[]
        for i in range(30):
            temp=sum([1 for c in candidates if (c>>i)&1])
            arr.append(temp)
        return max(arr)