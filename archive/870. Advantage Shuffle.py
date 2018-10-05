class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a = sorted([(x, i) for i, x in enumerate(A)])
        b = sorted([(x, i) for i, x in enumerate(B)])
        length = len(A)
        remain = []
        order = []
        i_a = i_b = 0
        while i_a < length and i_b < length:
            if a[i_a][0] <= b[i_b][0]:
                remain.append(a[i_a][1])
                i_a += 1
            else:
                order.append((a[i_a][1], b[i_b][1]))
                i_a += 1
                i_b += 1
        for i in range(len(remain)):
            order.append((remain[i], b[i_b + i][1]))
        ans = [None] * length
        for x, y in order:
            ans[y] = A[x]
        return ans


A = [12, 24, 8, 32]
B = [13, 25, 32, 11]
A = [2,7,11,15]
B = [1,10,4,11]
print(Solution().advantageCount(A, B))
