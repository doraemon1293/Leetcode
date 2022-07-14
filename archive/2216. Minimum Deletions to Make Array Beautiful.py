class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        p=0
        length=len(nums)
        new_arr=[nums[0]]
        deletion=0
        for num in nums[1:]:
            if len(new_arr)%2==1:
                if num==new_arr[-1]:
                    deletion+=1
                else:
                    new_arr.append(num)
            else:
                new_arr.append(num)
        if len(new_arr)%2==1:
            deletion+=1
        return deletion




