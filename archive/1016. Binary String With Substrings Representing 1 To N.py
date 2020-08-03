class Solution:
    def queryString(self, S: str, N: int) -> bool:
        max_len = len(bin(N)) - 2
        s = set(range(1, N + 1))
        for length in range(1, min(max_len + 1, len(S)+1)):
            for st in range(0, len(S) - length + 1):
                v =int(S[st:st + length],2)
                print(v)
                s.discard(v)
        print(s)
        return len(s)==0

S="0110"
N=3
print(Solution().queryString(S,N))