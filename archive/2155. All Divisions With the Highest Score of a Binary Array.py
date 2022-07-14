class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        pre_sum=0
        summ=sum(nums)
        div_scroe=summ
        idxs=[0]
        for i in range(1,len(nums)+1):
            num=nums[i-1]
            left=pre_sum+num
            right=summ-left
            temp=(i+1)-left+right
            if temp>div_scroe:
                div_scroe=temp
                idxs=[i]
            elif temp==div_scroe:
                idxs.append(i)
        return idxs









