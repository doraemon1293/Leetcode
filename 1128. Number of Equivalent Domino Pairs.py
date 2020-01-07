import collections
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter=collections.Counter([tuple(sorted(domino)) for domino in dominoes])
        ans=sum([v*(v-1)//2 for v in counter.values])
        return ans