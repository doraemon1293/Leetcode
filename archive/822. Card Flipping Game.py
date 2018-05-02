class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        not_allowed_numbers=set()
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                not_allowed_numbers.add(fronts[i])
        ans=float("inf")
        for i in range(len(fronts)):
            if fronts[i] not in not_allowed_numbers:
                ans=min(ans,fronts[i])
            if backs[i] not in not_allowed_numbers:
                ans=min(ans,backs[i])

        return ans if ans!=float("inf") else 0
