class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        mins = targetSeconds // 60
        secs = targetSeconds % 60
        target = (str(mins) + str(secs).zfill(2)).lstrip("0")
        print(target)

        def calc_cost(target):
            res = 0
            at = str(startAt)
            for ch in target:
                if at != ch:
                    res += moveCost
                    at = ch
                res += pushCost
            return res
        ans=calc_cost(target)

        if mins>1 and secs+60<=99:
            target = (str(mins-1) + str(secs+60).zfill(2)).lstrip("0")
            ans = min(ans,calc_cost(target))
        return ans

