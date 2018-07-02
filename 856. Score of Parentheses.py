class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        score=[]
        for ch in S:
            if ch=="(":
                score.append(0)
            else:
                if score[-1]==0:
                    score[-1]=1
                else:
                    temp=0
                    while score[-1]!=0:
                        temp+=score.pop()
                    score[-1]=2*temp
        return sum(score)