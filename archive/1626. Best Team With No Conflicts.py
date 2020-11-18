from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N=len(scores)
        scores = sorted([(a, s) for s, a in zip(scores, ages)])
        scores = [x[1] for x in scores]
        arr=scores[:]
        for i in range(N):
            maxi = 0
            for j in range(i):
                if scores[j]<=scores[i]:
                    maxi=max(maxi,arr[j])
            arr[i]=maxi+scores[i]
        return max(arr)







