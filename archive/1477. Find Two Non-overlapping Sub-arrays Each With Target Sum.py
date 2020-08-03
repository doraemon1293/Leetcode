from typing import List
import bisect
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        N = len(arr)
        left = right = 0
        temp = 0
        ans=mini_length=float("inf")
        mini_length_arr=[]
        while right < N:
            while right < N and temp < target:
                temp += arr[right]
                right += 1
            if temp == target:
                ind=bisect.bisect_right(mini_length_arr, (left,0))-1
                if ind>=0:
                    ans=min(ans,right-left+mini_length_arr[ind][1])
                mini_length=min(mini_length,right-left)
                mini_length_arr.append((right - 1,mini_length))

            while left <= right and temp >= target:
                temp -= arr[left]
                left += 1
                if temp == target:
                    ind = bisect.bisect_right(mini_length_arr, (left, 0)) - 1
                    if ind >= 0:
                        ans = min(ans, right - left + mini_length_arr[ind][1])
                    mini_length = min(mini_length, right - left)
                    mini_length_arr.append((right - 1, mini_length))
        return ans if ans!=float("inf") else -1

arr=[1,2,3,3,3]
target=6
print(Solution().minSumOfLengths(arr,target))