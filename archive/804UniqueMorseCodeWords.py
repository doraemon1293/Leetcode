class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans=set()
        for word in words:
            s="".join([morse[ord(ch)-ord("a")] for ch in word])
            ans.add(s)
        return len(ans)
words = ["gin", "zen", "gig", "msg"]
print(Solution().uniqueMorseRepresentations(words))