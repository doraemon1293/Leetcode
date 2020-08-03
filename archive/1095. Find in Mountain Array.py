# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        d={}
        def get(i):
            if i in d:
                return d[i]
            else:
                d[i]=mountain_arr.get(i)
                return d[i]

        left,right=0,mountain_arr.length()
        while left<=right:
            mid=(left+right)//2
            if get(mid)<get(mid+1):
                left=mid+1
            elif get(mid-1)>get(mid):
                right=mid-1
            elif get(mid-1)<get(mid) and get(mid)>get(mid+1):
                peak=mid
                break
        left,right=0,peak
        while left<=right:
            mid=(left+right)//2
            if get(mid)==target:
                return mid
            elif get(mid)<target:
                left=mid+1
            else:
                right=mid-1
        left,right=peak,mountain_arr.length()
        while left<=right:
            mid=(left+right)//2
            if get(mid)==target:
                return mid
            elif get(mid)>target:
                left=mid+1
            else:
                right=mid-1
        return -1


