class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(arr):
            if len(arr)==1:
                return arr
            mid=arr[len(arr)//2]
            left=[]
            right=[]
            for i in range(len(arr)):
                if i!=mid:
                    if arr[i]<arr[mid]:
                        left.append(arr[i])
                    else:
                        right.append(arr[i])
            return quicksort(left)+[arr[mid]]+quicksort(right)
        return quicksort(nums)