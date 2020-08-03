import collections
import bisect


class Solution:
    def numSmallerByFrequency(self, queries: list, words: list) -> list:
        queries = [collections.Counter(q)[min(q)] for q in queries]
        words = sorted([collections.Counter(w)[min(w)] for w in words])
        ans = [len(words) - bisect.bisect_right(words, q) for q in queries]
        return ans


queries = ["bba", "abaaaaaa", "aaaaaa", "bbabbabaab", "aba", "aa", "baab", "bbbbbb", "aab", "bbabbaabb"]
words = ["aaabbb", "aab", "babbab", "babbbb", "b", "bbbbbbbbab", "a", "bbbbbbbbbb", "baaabbaab", "aa"]
print(Solution().numSmallerByFrequency(queries, words))
