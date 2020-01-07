# |a-b|可以看成是 Math.max(a-b,b-a)；
#
# 先将|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|写成|a1 - b1| + |a2 - b2| + |i - j|， 以方便观看
#
# 我们将按索引顺序遍历数组，那么 |i - j|实际就是(i - j)
#
# |a1 - b1| + |a2 - b2| + (i - j)可以写成以下4个算式的最大值：
#
# (a1-b1) + (a2-b2) + (i-j)
# (a1-b1) + (b2-a2) + (i-j)
# (b1-a1) + (a2-b2) + (i-j)
# (b1-a1) + (b2-a2) + (i-j)
# 也可以写成:
#
# (+a1+a2+i) - (+b1+b2+j)
# (+a1-a2+i) - (+b1-b2+j)
# (-a1+a2+i) - (-b1+b2+j)
# (-a1-a2+i) - (-b1-b2+j)
# a1,a2 / b1,b2对应的符号分别是
#
# +,+
# +,-
# -,+
# -,-
# 因此只需要遍历4中符号，然后取最大值。


class Solution:
    def maxAbsValExpr(self, arr1: list, arr2: list) -> int:

        ans = -float("inf")
        for sig1, sig2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            max_v = -float("inf")
            min_v = float("inf")
            for i in range(len(arr1)):
                v = arr1[i] * sig1 + arr2[i] * sig2 + i
                max_v = max(max_v, v)
                min_v = min(min_v, v)
                ans = max(ans, max_v - min_v)
        return ans


arr1 = [1, 2, 3, 4]
arr2 = [-1, 4, 5, 6]
print(Solution().maxAbsValExpr(arr1, arr2))
