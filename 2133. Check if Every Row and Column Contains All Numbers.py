class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        N=len(matrix)
        for row in matrix:
            if len(set(row))!=N:
                return False
        for col in zip(*matrix):
            if len(set(col))!=N:
                return False
        return True

matrix = [[1,2,3],[3,1,2],[2,3,1]]
print(list(zip(*matrix)))