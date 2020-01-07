class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        pre_sum=0
        d={0:1}
        for a in A:
            pre_sum=(pre_sum+a)%K
            d.setdefault(pre_sum,0)
            d[pre_sum]+=1
        return sum(v*(v-1)//2 for v in d.values())

