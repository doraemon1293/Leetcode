from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

        self.subrectangle = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.subrectangle.append([row1, col1, row2, col2, newValue])

    def getValue(self, row: int, col: int) -> int:
        for i in range(len(self.subrectangle) - 1, -1, -1):
            x1, y1, x2, y2, val = self.subrectangle[i]
            if x1 <= row <= x2 and y1 <= col <= y2:
                return val
        return self.rectangle[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
