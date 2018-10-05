class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        rightest={tree[0]:0}
        left_ind=0
        ans=1
        for ind in range(1,len(tree)):
            rightest[tree[ind]] = ind
            if len(rightest)<=2:
                ans = max(ans, ind - left_ind + 1)
            else:
                left_type=min([(v,k) for k,v in rightest.items()])[1]
                left_ind=rightest[left_type]+1
                del rightest[left_type]
        return ans

tree=[1,0,1,4,1,4,1,2,3]
print(Solution().totalFruit(tree))