import collections


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # words = set(words)
        d = collections.defaultdict(set)
        max_length = {}
        ans = 1
        for word in words:
            d[len(word)].add(word)
            max_length[word] = 1
        for length in sorted(d.keys()):
            for w2 in d[length]:
                for i in range(len(w2)):
                    w1 = w2[:i] + w2[i + 1:]
                    if w1 in d[length - 1]:
                        max_length[w2] = max(max_length[w2], max_length[w1] + 1)
                        ans = max(ans, max_length[w2])
        return ans
