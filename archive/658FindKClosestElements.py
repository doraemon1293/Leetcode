# coding=utf-8
'''
Created on 2017å¹?8æœ?13æ—?

@author: Administrator
'''


class Solution(object):

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        import bisect
        ind = bisect.bisect(arr, x)
        if ind == len(arr):
            ind -= 1
        elif ind == 0:
            pass
        else:
            if abs(arr[ind - 1] - x) <= abs(arr[ind] - x):
                ind -= 1
        print ind
        st = en = ind
        while en - st < k - 1:
            if st == 0:
                en += 1
            elif en == len(arr) - 1:
                st -= 1
            else:
                if abs(arr[st - 1] - x) <= abs(arr[en + 1] - x):
                    st -= 1
                elif abs(arr[en + 1] - x) < abs(arr[st - 1] - x):
                    en += 1
            print st, en
        return arr[st:en + 1]


arr = [0, 0, 0, 1, 3, 5, 6, 7, 8, 8]
k = 2
x = 2
print Solution().findClosestElements(arr, k, x)

