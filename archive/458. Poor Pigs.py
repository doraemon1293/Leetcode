class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """

        import math
        p = math.log(buckets, minutesToTest / minutesToDie + 1)
        return int(math.ceil(p))