class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        def foo(S, word):
            p1 = p2 = 0
            l1 = len(S)
            l2 = len(word)

            while p1 < l1 and p2 < l2:
                ch1 = S[p1]
                c1 = 0
                while p1 < l1 and S[p1] == ch1:
                    c1 += 1
                    p1 += 1

                ch2 = word[p2]
                c2 = 0
                while p2 < l2 and word[p2] == ch2:
                    c2 += 1
                    p2 += 1

                if ch1 == ch2 and (c1 >= 3 and c1 > c2 or c1==c2):
                    pass
                else:
                    return False

            if p1 == l1 and p2 == l2:
                return True
            else:
                return False

        return sum([foo(S, word) for word in words])
S = "heeellooo"
words = ["hello", "hi", "helo"]
print(Solution().expressiveWords(S,words))