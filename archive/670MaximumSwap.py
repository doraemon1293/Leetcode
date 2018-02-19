class Solution(object):

    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        for i in xrange(len(num)):
            maxi = num[i]
            for j in xrange(len(num) - 1, i, -1):
                if num[j] > maxi:
                    maxi = num[j]
                    k = j
            if maxi != num[i]:
                num[i], num[k] = num[k], num[i]
                break
        return int("".join(num))


num = 2736
print Solution().maximumSwap(num)
