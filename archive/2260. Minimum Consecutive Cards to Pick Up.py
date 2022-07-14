import collections
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d={}
        ans=float("inf")
        for i,card in enumerate(cards):
            if card in d:
                ans=min(i-d[card]+1,ans)
            d[card]=i
        return -1 if ans==float("inf") else ans