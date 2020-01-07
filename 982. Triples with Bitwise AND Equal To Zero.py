#容斥原理
from collections import defaultdict


class Solution:
    def countTriplets(self, A: 'List[int]') -> 'int':
        N = len(A)
        one = defaultdict(set)
        for ind in range(N):
            for i in range(16):
                if A[ind] >> i & 1:
                    one[i].add(ind)
        sets = list(one.values())
        venn = [[] for _ in range(len(sets))]
        for i in range(len(sets)):
            s1 = sets[i]
            for j in range(i - 1, -1, -1):
                for s2 in venn[j]:
                    s12 = s1 & s2
                    if s12:
                        venn[j + 1].append(s12)
            venn[0].append(s1)
        counts = 0
        for i in range(len(venn)):
            for s in venn[i]:
                counts += ((-1) ** i) * (len(s) ** 3)
        return N ** 3 - counts


A = [2, 4, 7, 3, 11]
print(Solution().countTriplets(A))
