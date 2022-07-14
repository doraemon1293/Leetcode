class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N=len(questions)
        dp=[0]*N
        def score(ind):
            if ind>=N:
                return 0
            else:
                return dp[ind]
        for i in range(N-1,-1,-1):
            points,cost=questions[i]
            dp[i]=max(score(i+1),points+score(i+cost+1))
        return dp[0]
            