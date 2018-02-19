# coding=utf-8
'''
Created on 2017å¹?7æœ?5æ—?

@author: Administrator
'''

nums = [1, 2, 3, 4, 5, 6]
num = 1.9
st, en = 0, len(nums) - 1
ans = None
while st <= en:
    mid = (st + en) / 2
    if nums[mid] < num:
        st = mid + 1
    elif nums[mid] > num:
        en = mid - 1
    else:
        ans = mid
        break
print st, en, ans
