class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words=S.split(" ")
        ans=[]
        for i,word in enumerate(words):
            if word[0] in ("a","A","e","E","i","I","o","O","u","U"):
                word+="ma"
            else:
                word=word[1:]+word[0]+"ma"
            word+="a"*(i+1)
            ans.append(word)
        return " ".join(ans)
S="The quick brown fox jumped over the lazy dog"
print(Solution().toGoatLatin(S))