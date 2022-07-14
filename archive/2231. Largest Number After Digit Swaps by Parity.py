class Solution:
    def largestInteger(self, num: int) -> int:
        num=[int(ch) for ch in str(num)]
        odds=[]
        odds_ind=[]
        evens=[]
        evens_ind=[]
        for i,x in enumerate(num):
            if x%2==0:
                evens.append(x)
                evens_ind.append(i)
            else:
                odds.append(x)
                odds_ind.append(i)

        odds.sort(reverse=True)
        evens.sort(reverse=True)
        odds_ind.sort()
        evens_ind.sort()

        ans=[None]*len(num)
        for x, i in zip(odds,odds_ind):
            ans[i]=str(x)
        for x, i in zip(evens,evens_ind):
            ans[i]=str(x)
        return "".join(ans)

