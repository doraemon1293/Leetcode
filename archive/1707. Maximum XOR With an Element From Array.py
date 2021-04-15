from typing import List
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums = sorted(nums)
        ans=[-1]*len(queries)
        queries=sorted(enumerate(queries),key=lambda x:x[1][1])
        root={}
        def insert(num):
            child=root
            for i in range(32,-1,-1):
                k=(num>>i)&1
                child.setdefault(k,{})
                child=child[k]
            child["#"]=num

        def find(x):
            child=root
            for i in range(32,-1,-1):
                k=((x>>i)&1)^1
                if k in child:
                    child=child[k]
                elif k^1 in child:
                    child=child[k^1]
                else:
                    return -1
            return child['#']

        num_ind=0
        for query in queries:
            ind=query[0]
            x, m = query[1]
            while num_ind<len(nums) and nums[num_ind]<=m:
                insert(nums[num_ind])
                num_ind+=1
            temp=find(x)
            ans[ind]=temp if temp==-1 else temp^x
        return ans

print(Solution().maximizeXor([0,1,2,3,4],
[[3,1],[1,3],[5,6]]))

            

