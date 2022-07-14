# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left, right = 0, reader.length() - 1
        while left < right:
            length = right - left + 1
            print(left, right, length)
            if length % 2 == 0:
                res = reader.compareSub(left, left + length // 2 - 1, right - length // 2 + 1, right)
                if res > 0:
                    left, right = left, left + length // 2 - 1
                else:
                    left, right = right - length // 2 + 1, right
            else:
                res = reader.compareSub(left, left + length // 2 - 1, right - length // 2 + 1, right)
                if res > 0:
                    left, right = left, left + length // 2 - 1
                elif res < 0:
                    left, right = right - length // 2 + 1, right
                else:
                    return left + length//2
        return left

