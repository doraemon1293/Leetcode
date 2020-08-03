class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        cur_chars = set()
        st = end = 0
        ans = 0
        while st < len(S):
            while end < len(S) and S[end] not in cur_chars and len(cur_chars) < K:
                cur_chars.add(S[end])
                end += 1
            if len(cur_chars) == K:
                ans += 1
            cur_chars.discard(S[st])
            st += 1
        return ans


S = "havefunonleetcode"
K = 5
S="home"
K=5
print(Solution().numKLenSubstrNoRepeats(S, K))
