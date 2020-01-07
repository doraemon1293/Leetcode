import collections


class Solution:
    def findNumOfValidWords(self, words: list, puzzles: list) -> list:
        c_words = collections.defaultdict(int)

        for word in words:
            s = frozenset(word)
            if len(s) <= 7:
                mask = 0
                for ch in s:
                    mask |= 1 << ord(ch) - ord("a")
                c_words[mask] += 1
        ans = []

        def foo(puzzle):
            all_masks = set([1 << (ord(puzzle[0]) - ord('a'))])
            for ch in puzzle[1:]:
                new_masks = set()
                for mask in all_masks:
                    new_masks.add(mask | (1 << (ord(ch) - ord('a'))))
                all_masks=all_masks|new_masks
            return sum(c_words[mask] for mask in all_masks)

        for puzzle in puzzles:
            ans.append(foo(puzzle))
        return ans

        # solution 1 真值表转逻辑表达式 TLE
        # def foo(a, b):
        #     return (~a & ~b) | (a & b) | (~a & b)
        #
        # for puzzle in puzzles:
        #     temp=0
        #     for mask_w in c_words:
        #         ch = puzzle[0]
        #         if (mask_w >> (ord(ch) - ord("a"))) & 1:
        #             mask_p = 0
        #             for ch in puzzle:
        #                 mask_p |= 1 << (ord(ch) - ord("a"))
        #             if ~foo(mask_w, mask_p) ==0:
        #                 temp+=c_words[mask_w]
        #     ans.append(temp)
        # return ans
words=["aaaa","asas","able","ability","actt","actor","access"]
puzzles=["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]

print(Solution().findNumOfValidWords(words, puzzles))
