class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        start = bin(start)[2:].zfill(30)
        goal = bin(goal)[2:].zfill(30)
        # print(start,goal)
        return len([1 for a, b in zip(start, goal) if a != b])
