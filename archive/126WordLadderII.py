# coding=utf-8
'''
Created on 2017å¹?7æœ?4æ—?

@author: Administrator
'''

# coding=utf-8
'''
Created on 2017å¹?7æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if wordList == [] or endWord not in wordList: return []
        from collections import defaultdict
        word_length = len(wordList[0])
        wordList = set(wordList)
        wordList.discard(beginWord)
        d = defaultdict(set)
        for word in wordList:
            for i in xrange(word_length):
                s = word[:i] + "_" + word[i + 1:]
                d[s].add(word)
        parents = defaultdict(set)
        cur_level = {beginWord}
        while cur_level and endWord not in cur_level:
            next_level = defaultdict(set)
            for word in cur_level:
                for i in xrange(word_length):
                    s = word[:i] + "_" + word[i + 1:]
                    for word1 in d.get(s, []):
                        if word1 not in parents:
                            next_level[word1].add(word)
            cur_level = next_level
            parents.update(next_level)
        if endWord not in parents: return []
        res = [[endWord]]
        while res[0][0] != beginWord:
            res = [[p] + r for r in res for p in parents[r[0]]]
        return res


beginWord = "red"
endWord = "tax"
wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
# beginWord = "qa"
# endWord = "sq"
# wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print Solution().ladderLength(beginWord, endWord, wordList)

