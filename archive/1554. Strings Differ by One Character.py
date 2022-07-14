from typing import List
import collections


class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        d = collections.defaultdict(set)
        # for w in dict:
        #     print(w)
        MOD = 10 ** 13 + 7
        for i, word in enumerate(dict):
            val = 0
            unit = 1
            for ch in word:
                val = (val + unit * (ord(ch) - ord("a")+1)) % MOD
                unit = (unit * 27) % MOD
            # print(val, word)
            unit = 1
            for ch in word:
                new_val = (val - unit * (ord(ch) - ord("a")+1)) % MOD
                # print(word, ch, new_val)
                unit = (unit * 27) % MOD
                d[new_val].add(val)
                if len(d[new_val]) > 1:
                    return True
        return False