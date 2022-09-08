class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        root={}
        summ={}

        def find(x):
            path=[x]
            while x!=root[x]:
                x=root[x]
                path.append(x)
            for node in path:
                root[node]=x
            return x

        def union(x,y):
            root_x,root_y=find(x),find(y)
            root[root_x]=root_y
            summ[root_y]+=summ[root_x]

        ans=[]
        maxi=0
        for ind in removeQueries[::-1]:
            ans.append(maxi)
            root[ind]=ind
            summ[ind]=nums[ind]
            maxi=max(maxi,nums[ind])
            if ind-1 in root:
                union(ind-1,ind)
                maxi=max(maxi,summ[find(ind)])
            if ind+1 in root:
                union(ind,ind+1)
                maxi=max(maxi,summ[find(ind)])
        return ans[::-1]

