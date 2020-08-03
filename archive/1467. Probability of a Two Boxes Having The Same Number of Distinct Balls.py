from typing import List
from functools import lru_cache


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        self.num = 0

        N = len(balls)
        space_in_each_box = sum(balls) // 2

        @lru_cache(None)
        def comb(x, y):  # x<=y
            res = 1
            for i in range(x):
                res *= y - i
            for i in range(1, x + 1):
                res //= i
            return res

        @lru_cache(None)
        def get_permunation_number(balls_array):
            # print(balls_array)
            summ = sum(balls_array)
            res = 1
            for ball in balls_array:
                res *= comb(ball, summ)
                summ -= ball
            # print(res)
            return res

        def dfs(cur_no, space_box1, colour_box1, colour_box2, balls_array):
            if space_box1 == 0:
                colour_box2 += N - cur_no
                if colour_box1 == colour_box2:
                    balls_array1=balls_array
                    balls_array2=[balls[i]-(balls_array[i] if i<len(balls_array) else 0) for i in range(N)]

                    balls_array1 = tuple(sorted([x for x in balls_array1 if x!=0]))
                    balls_array2 = tuple(sorted([x for x in balls_array2 if x != 0]))

                    temp1 = get_permunation_number(balls_array1)
                    temp2 = get_permunation_number(balls_array2)
                    self.num += temp1*temp2

            else:
                if cur_no < N:
                    for i in range(min(space_box1+1, balls[cur_no]+1)):
                        if i == 0:
                            dfs(cur_no + 1, space_box1, colour_box1, colour_box2 + 1, balls_array+[0])
                        elif i == balls[cur_no]:
                            dfs(cur_no + 1, space_box1 - i, colour_box1 + 1, colour_box2, balls_array + [i])
                        else:
                            dfs(cur_no + 1, space_box1 - i, colour_box1 + 1, colour_box2 + 1, balls_array + [i])
        self.den=get_permunation_number(tuple(sorted(balls)))
        dfs(0, space_in_each_box, 0, 0, [])
        return self.num / self.den

balls=[1,1]
balls= [2,1,1]
balls = [6, 6, 6, 6, 6, 6,6,6]
print(Solution().getProbability(balls))
