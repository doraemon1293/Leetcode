import collections


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        old_words = words[:]
        words = [collections.Counter(w) for w in words]
        arr = [words[0]]
        ans = [0]

        for i in range(1, len(words)):
            if words[i] == arr[-1]:
                continue
            else:
                ans.append(i)
                arr.append(words[i])
        ans = [old_words[x] for x in ans]
        return ans

