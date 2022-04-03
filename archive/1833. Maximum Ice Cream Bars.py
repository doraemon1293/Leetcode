
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        ans=0
        for cost in costs:
            if cost<=coins:
                coins-=cost
                ans+=1
            else:
                break
        return ans