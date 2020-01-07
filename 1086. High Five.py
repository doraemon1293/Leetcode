class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d={}
        for id_,score in items:
            d.setdefault(id_,[])
            d[id_].append(score)
        ans=[]
        for k in sorted(d):
            ans.append([k,sum(sorted(d[k],reverse=True)[:5])/min(5,len(d[k]))])
        return ans
