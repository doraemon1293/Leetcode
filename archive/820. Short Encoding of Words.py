class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        set_words=set(words)
        for word in words:
            for i in range(1,len(word)):
                if word[i:] in set_words:
                    set_words.remove(word[i:])
        return sum([len(word)+1 for word in set_words])

