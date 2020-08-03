import math


class Solution:
    def pathInZigZagTree(self, label: int) -> list:
        row = int(math.ceil(math.log2(label + 1)))
        ans = []
        print(row)
        def f(n, row):
            if row == 1:
                ans.append(1)
            else:
                ans.append(n)
                next_n = 2 ** (row - 2) + (2 ** (row - 2) - 1) - (n - 2 ** (row - 1)) // 2
                next_row = row - 1
                print(next_row,next_n)
                f(next_n, next_row)
        f(label,row)
        return ans[::-1]
label=26
print(Solution().pathInZigZagTree(label))
