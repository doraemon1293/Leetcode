import collections


class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {"": 1}
        MOD = 10 ** 9 + 7
        for _ in range(n):
            new_d = collections.defaultdict(int)
            for ch in d:
                if ch == "":
                    for t in ("a", "e", "i", "o", "u"):
                        new_d[t] += 1
                if ch == "a":
                    new_d["e"] += d[ch] % MOD
                if ch == "e":
                    new_d["a"] += d[ch] % MOD
                    new_d["i"] += d[ch] % MOD
                if ch == "i":
                    new_d["a"] += d[ch] % MOD
                    new_d["e"] += d[ch] % MOD
                    new_d["o"] += d[ch] % MOD
                    new_d["u"] += d[ch] % MOD
                if ch == "o":
                    new_d["i"] += d[ch] % MOD
                    new_d["u"] += d[ch] % MOD
                if ch == "u":
                    new_d["a"] += d[ch] % MOD
            d = new_d

        return sum(d.values()) % MOD


n=10
print(Solution().countVowelPermutation(n))