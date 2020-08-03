class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        fc=[set(x) for x in favoriteCompanies]
        ans=[]
        for i in range(len(fc)):
            flag=True
            for j in range(len(fc)):
                if i!=j:
                    if len(fc[i]-fc[j])==0:
                        flag=False
                        break
            if flag:
                ans.append(i)
        return ans


            