class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        d={}
        for i,j,k in bookings:
            d.setdefault(i,0)
            d.setdefault(j+1,0)
            d[i]+=k
            d[j+1]-=k
        ans=[None]
        cur=0
        for i in range(1,n+1):
            if i in d:
                cur+=d[i]
            ans.append(cur)
        return ans[1:]