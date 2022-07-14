class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        p, m = power, modulo
        pk_mod_m = [1]
        for i in range(k - 1):
            pk_mod_m.append((pk_mod_m[-1] * p) % m)
        N = len(s)
        sub = s[N - k:]
        val = sum([(ord(ch) - ord("a") + 1) * pk_mod_m[i] for i, ch in enumerate(sub)]) % m
        if val == hashValue:
            ans=sub
        for i in range(N - k - 1, -1, -1):
            val = ((val - (ord(s[i + k]) - ord("a") + 1) * pk_mod_m[k - 1]) * p + (ord(s[i]) - ord("a") + 1)) % m
            if val == hashValue:
                ans = s[i:i + k]
        return ans


print(Solution().subStrHash("bzzrtrrpppigevriaooetwawtnfwddgdvoldxucsbyaufhygdxpnxupmvwbryzlgiuierypzqvwiywqlwiygyj",
76,
4,
60,
2))
