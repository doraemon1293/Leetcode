class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split(" ")
        s=sorted([(int(word[-1]),word[:-1]) for word in s])
        return " ".join([x[1] for x in s])