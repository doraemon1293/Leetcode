
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        return [num for num in c if c[num]==1 and num-1 not in c and num+1 not in c]