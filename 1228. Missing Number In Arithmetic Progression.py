class Solution(object):
    def missingNumber(self, a):
        """
        :type arr: List[int]
        :rtype: int
        """
        diff = (a[-1] - a[0]) // len(a)
        lo, hi = 0, len(a) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            temp = a[0] + mid * diff
            if temp == a[mid]:
                lo = mid + 1
            if temp != a[mid]:
                hi = mid
        return a[lo]-diff


a = [1, 2, 3, 4, 5, 6, 8]
a=[15,13,12]
print(Solution().missingNumber(a))
