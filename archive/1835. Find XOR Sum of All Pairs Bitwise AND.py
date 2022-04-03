class Solution(object):
    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        xor_all_arr2=arr2[0]
        for num in arr2[1:]:
            xor_all_arr2^=num
        ans=arr1[0]&xor_all_arr2
        for num in arr1[1:]:
            ans^=num&xor_all_arr2
        return ans