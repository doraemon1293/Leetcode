from collections import Counter
import copy


class Solution:
    def maxScoreWords(self, words: list, letters: list, score: list) -> int:
        word_score = [sum([score[ord(ch) - ord('a')] for ch in word]) for word in words]
        word_ch = [Counter(word) for word in words]
        letters = Counter(letters)

        def dfs(ind, letters):
            if ind == len(words):
                return 0
            a = dfs(ind + 1, letters)
            new_letters = {}
            f = True

            for k in set(list(letters.keys()) + list(word_ch[ind].keys())):
                new_letters[k] = letters.get(k, 0) - word_ch[ind].get(k, 0)
                if new_letters[k] < 0:
                    f = False
                    break
            if f:
                b = word_score[ind] + dfs(ind + 1, new_letters)
            else:
                b = -1

            return max(a, b)

        return dfs(0, letters)


words = ["dog", "cat", "dad", "good"]
letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(Solution().maxScoreWords(words, letters, score))
