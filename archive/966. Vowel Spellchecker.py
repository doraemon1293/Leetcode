class Solution:
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """

        def blur_vowel(word):
            return "".join(["*" if ch in ("a", "e", "i", "o", "u") else ch for ch in word.lower()])

        wordlist_set = set()
        wordlist_case_nonsensetive = {}
        wordlist_vowel_nonsensetive = {}
        for word in wordlist:
            wordlist_set.add(word)
            wordlist_case_nonsensetive.setdefault(word.lower(), word)
            wordlist_vowel_nonsensetive.setdefault(blur_vowel(word), word)
        ans = []
        print(wordlist_case_nonsensetive)
        print(wordlist_vowel_nonsensetive)
        for query in queries:
            if query in wordlist_set:
                ans.append(query)
                continue
            if query.lower() in wordlist_case_nonsensetive:
                ans.append(wordlist_case_nonsensetive[query.lower()])
                continue
            blured_query = blur_vowel(query)
            if blured_query in wordlist_vowel_nonsensetive:
                ans.append(wordlist_vowel_nonsensetive[blured_query])
                continue
            ans.append("")
        return ans


wordlist = ["KiTe", "kite", "hare", "Hare"]
queries = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
print(Solution().spellchecker(wordlist, queries))
