import collections
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        N = len(words[0])
        last = [0] * N
        last_sum = [0] * N
        counters = []
        MOD = 10 ** 9 + 7
        summ = 0
        for i in range(N):
            counters.append(collections.Counter([word[i] for word in words]))
            last_sum[i] = summ
            last[i] = counters[i].get(target[0], 0)
            summ += last[i]

        for i in range(1, len(target)):
            ch = target[i]
            summ = 0
            new = [0] * N
            new_sum = [0] * N
            for j in range(len(last)):
                new_sum[j] = summ
                counter = counters[j]
                new[j] = last_sum[j] * counter.get(ch,0) % MOD
                summ = (summ + new[j]) % MOD
            last, last_sum = new, new_sum
        return (last_sum[-1]+last[-1]) % MOD


words = ["abab",
         "baba",
         "abba",
         "baab"]

target = "abba"
print(Solution().numWays(words, target))
