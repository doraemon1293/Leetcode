from typing import List
from collections import defaultdict
import functools


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        hats_to_people = defaultdict(list)
        number_of_people = len(hats)
        for p, hats_ in enumerate(hats):
            for hat in hats_:
                hats_to_people[hat].append(p)
        hats_to_people = list(hats_to_people.values())
        number_of_hats = len(hats_to_people)
        if number_of_hats < number_of_people:
            return 0
        print(hats_to_people)
        @functools.lru_cache(None)
        def dp(hat, mask):
            if hat == number_of_hats and bin(mask).count("1") == number_of_people:
                return 1
            if number_of_people - bin(mask).count("1") > number_of_hats - hat:
                return 0
            # end condition
            res = 0
            res += dp(hat + 1, mask)
            for p in hats_to_people[hat]:
                if (mask>>p)&1==0:
                    new_mask = mask | (1 << p)
                    res += dp(hat + 1, new_mask)
            return res%MOD

        return dp(0, 0)


hats = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
hats=[[3,5,1],[3,5]]
print(Solution().numberWays(hats))
