import math
class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        max_exp_x=int(math.log(bound,x) if x!=1 else 1)
        max_exp_y = int(math.log(bound, y) if y != 1 else 1)
        x_val=set([x**i for i in range(max_exp_x+1)])
        y_val = set([y ** i for i in range(max_exp_y + 1)])
        ans=set()
        for v1 in x_val:
            for v2 in y_val:
                if v1+v2<=bound:
                    ans.add(v1+v2)
        return ans


print(Solution().powerfulIntegers(1,2,100))