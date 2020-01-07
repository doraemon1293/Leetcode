class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sorrt()
        min_d=min([arr[i+1]-arr[i] for i in range(len(arr)-1)])
        ans=[(arr[i],arr[i+1]) for i in range(len(arr)-1) if arr[i+1]-arr[i]==min_d]
        return ans