import itertools


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """

        def minutes(p):
            if p == "":
                return -1
            return int(p[0] + p[1]) * 60 + int(p[2] + p[3])

        ans = ""
        A=[str(x) for x in A]
        for p in itertools.permutations(A):
            if int(p[0] + p[1]) < 24:
                if int(p[2] + p[3]) < 60:
                    if minutes(p) > minutes(ans):
                        ans = p
        return ans if ans=="" else ans[0]+ans[1]+":"+ans[2]+ans[3]