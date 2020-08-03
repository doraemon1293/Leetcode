class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d=dict((x,i) for i,x in enumerate(arr2))
        arr1.sort(key=lambda x:d.get(x,len(arr2)+x))
        return arr1