class Solution(object):

    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        ans = letters[0]
        for letter in letters:
            t1 = (ord(letter) - ord(target))
            if t1 <= 0:
                t1 += 26
            t2 = (ord(ans) - ord(target))
            if t2 <= 0:
                t2 += 26
            if t1 < t2:
                ans = letter

        return ans


letters = ["c", "f", "j"]
target = "c"
print Solution().nextGreatestLetter(letters, target)
