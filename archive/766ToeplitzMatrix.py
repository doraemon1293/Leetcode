class Solution:

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        for y0 in range(n):
            x0 = 0
            target = matrix[x0][y0]
            while x0 < m and y0 < n:
                if matrix[x0][y0] != target:
                    return False
                x0 += 1
                y0 += 1
        for x0 in range(m):
            y0 = 0
            target = matrix[x0][y0]
            while x0 < m and y0 < n:
                if matrix[x0][y0] != target:
                    return False
                x0 += 1
                y0 += 1
        return True


matrix = [[1, 2, 3, 4], [6, 1, 2, 3], [9, 5, 1, 2]]
print(Solution().isToeplitzMatrix(matrix))
