from typing import List
import collections
import functools
import math


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def divisors(num):
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    s = divisors(num // i)
                    return s | set([divisor * i for divisor in s])
            return {1, num}

        d = collections.defaultdict(list)
        for num in nums:
            for divisor in divisors(num):
                d[divisor].append(num)
        ans = 0
        for divisor in d:
            a = d[divisor][0]
            for num in d[divisor][1:]:
                a = math.gcd(a, num)
                if a==divisor:
                    break
            if a == divisor:
                ans += 1
        return ans