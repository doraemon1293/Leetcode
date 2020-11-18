class Solution(object):
    def countSmaller(self, nums):
        ans = [0] * len(nums)

        def mergeSort(enums):
            if len(enums)<2:
                return enums
            else:
                mid=len(enums)//2
                left=mergeSort(enums[:mid])
                right=mergeSort(enums[mid:])
                res=[]
                while left and right:
                    if left[-1][1]>right[-1][1]:
                        ans[left[-1][0]]+=len(right)
                        res.append(left.pop())
                    else:
                        res.append(right.pop())
                res=res[::-1]
                if left:
                    res=left+res
                elif right:
                    res=right+res
                return res
        enums=list(enumerate(nums))
        mergeSort(enums)
        return ans