class Solution(object):

    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        mini = float("inf")
        total_nut_to_tree = 0
        for nut in nuts:
            nut_to_tree = abs(nut[0] - tree[0]) + abs(nut[1] - tree[1])
            total_nut_to_tree += nut_to_tree
            nut_to_squrrel = abs(nut[0] - squirrel[0]) + abs(nut[1] - squirrel[1])
            if (nut_to_squrrel - nut_to_tree) < mini:
                mini = nut_to_squrrel - nut_to_tree
        return mini + total_nut_to_tree * 2


print Solution().minDistance(5,
7,
[2, 2],
[4, 4],
[[3, 0], [2, 5]])
