class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def solve(word,pattern):
            d={}
            s=set()
            for i in range(len(word)):
                if word[i] in d:
                    if pattern[i]!=d[word[i]]:
                        return False
                if word[i] not in d:
                    if pattern[i] not in s:
                        d[word[i]]=pattern[i]
                        s.add(pattern[i])
                    else:
                        return False
            return True
        return [word for word in words if solve(word)]

