from collections import defaultdict


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        same = defaultdict(int)
        a = defaultdict(int)
        b = defaultdict(int)
        total = defaultdict(int)
        same_num = 0
        N=len(A)
        for i in range(len(A)):
            if A[i] == B[i]:
                same[A[i]]+=1
                if len(same) > 1:
                    return -1
            else:
                a[A[i]] += 1
                b[B[i]] += 1
                total[A[i]] += 1
                total[B[i]] += 1
        if same:
            num=list(same.keys())[0]
            if total[num]==N-same[num]:
                return min(abs(N-same[num]-a[num]),abs(N-same[num]-b[num]))

            else:
                return -1
        else:
            candidates=[x for x in total.keys() if total[x]==N]
            if candidates:
                return min([min(abs(total[k]-a[k]),abs(total[k]-b[k])) for k in candidates])
            else:
                return -1

