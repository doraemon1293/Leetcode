class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        x=-1
        while x<0 or x>39:
            x=(rand7()-1)+7*(rand7()-1)
        return 1+x%10