class Solution(object):

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = ["0"]
        for _ in xrange(n):
            if _ == 0:
                ans += ["1"]
            else:
                ans = ans + ans[::-1]
                for i in xrange(len(ans)):
                    if i < len(ans) / 2:
                        ans[i] = "0" + ans[i]
                    else:
                        ans[i] = "1" + ans[i]
        return [int(x, 2) for x in ans]
# 镜射排列
