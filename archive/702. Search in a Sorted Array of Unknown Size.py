class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        hi=1
        while reader.get(hi)!=2147483647:
            hi*=2
        lo=0
        while lo <= hi:
            mid = (lo + hi) / 2
            val = reader.get(mid)
            if target == val:
                return mid
            elif target > val:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
