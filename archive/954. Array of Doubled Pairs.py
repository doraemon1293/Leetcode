from collections import defaultdict


class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort()
        d = defaultdict(set)
        for i, a in enumerate(A):
            d[a].add(i)
        for i, a in enumerate(A):
            if a != None:
                d[a].remove(i)
                if a>=0:
                    target = a * 2
                if a<0:
                    if a%2:
                        return False
                    else:
                        target=a//2
                if d[target]:
                    ind = d[target].pop()
                    A[ind] = None
                else:
                    return False
        return True


A = [1, 2, 4, 16, 8, 4]
# A = [4, -2, 2, -4]
A = [3, 1, 3, 6]
# A = [0, 0]
A=[-5,-3]
print(Solution().canReorderDoubled(A))
