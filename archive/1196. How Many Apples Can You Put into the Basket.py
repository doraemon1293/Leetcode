class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        temp = 0
        for i in range(len(arr)):
            temp += arr[i]
            if temp >= 5000:
                break
        return i if temp > 5000 else i + 1
