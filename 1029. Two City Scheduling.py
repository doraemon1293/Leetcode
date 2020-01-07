class Solution:
    def twoCitySchedCost(self, costs) -> int:
        diff=[(cost[0]-cost[1],i) for i, cost in enumerate(costs)]
        diff.sort()
        inds=set([x[1] for x in diff[:i]])
        ans=0
        for i in range(len(costs)):
            if i in inds:
                ans+=costs[i][0]
            else:
                ans+=costs[i][1]
        return ans



