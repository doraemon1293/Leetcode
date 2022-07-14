class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[num for num in nums if num>0]
        neg=[num for num in nums if num<0]
        ans=[]
        for a,b in zip(pos,neg):
            ans.append(a)
            ans.append(b)
        return ans