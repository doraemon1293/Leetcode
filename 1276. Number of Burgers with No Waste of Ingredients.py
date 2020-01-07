class Solution:
    def numOfBurgers(self, t: int, c: int) -> List[int]:
        # 4,1 2,1
        x = (t - 2 * c) / 2
        y = c - x
        if x >= 0 and y >= 0 and x == int(x) and y == int(y):
            return [int(x), int(y)]
        else:
            return []
