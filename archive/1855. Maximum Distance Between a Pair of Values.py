class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        p1=p2=0
        ans=0
        while p1<len(nums1):
            while p2<len(nums2) and nums2[p2]>=nums1[p1]:
                p2+=1
            ans=max(ans,p2-p1-1)
            p1+=1
        return ans