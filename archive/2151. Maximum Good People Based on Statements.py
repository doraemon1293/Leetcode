from typing import List
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        self.ans=-1
        n=len(statements)
        def dfs(k,status):
            if k==n:
                self.ans=max(self.ans,len([1 for i in range(n) if (status>>i)&1]))
            else:
                people=[(status>>i)&1 for i in range(k)]
                choices={0,1}
                for i in range(k):
                    #i--k
                    if people[i]==1:
                        if statements[i][k]==1:
                            choices.discard(0)
                        if statements[i][k]==0:
                            choices.discard(1)
                    #k--i
                    if statements[k][i]==1 and people[i]==0:
                        choices.discard(1)
                    if statements[k][i]==0 and people[i]==1:
                        choices.discard(1)
                for next_bit in choices:
                    new_status=(status|(next_bit<<k))
                    dfs(k+1,new_status)
        dfs(0,0)
        return self.ans






statements = [[2,1,2],[1,2,2],[2,0,2]]
statements = [[2,0],[0,2]]
print(Solution().maximumGood(statements))