class Solution(object):

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i = 0
        j = len(s) - 1

        while i < j:
            while s[i].lower() not in ("a", "e", "i", "o", "u") and i < j:
                i += 1
            while s[j].lower() not in ("a", "e", "i", "o", "u") and i < j:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)


s = "hello"
print Solution().reverseVowels(s)
