class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        queens = set([tuple(x) for x in queens])
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):
            x0, y0 = king
            x1, y1 = x0, y0
            goon = True
            while goon:
                x1, y1 = x1 + dx, y1 + dy
                if 0 <= x1 <= 8 and 0 <= y1 <= 8:
                    if (x1, y1) in queens:
                        ans.append([x1, y1])
                        goon=False
                else:
                    goon = False
        return ans
