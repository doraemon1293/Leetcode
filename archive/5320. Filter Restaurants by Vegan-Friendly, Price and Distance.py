import bisect
class Solution:
    def filterRestaurants(self, restaurants: list, veganFriendly: int, maxPrice: int, maxDistance: int) -> list:
        ans=[]
        for id_,rating,v,p,dis in restaurants:
            if (veganFriendly and v or veganFriendly==0) and p<=maxPrice and dis<=maxDistance:
                ans.append([rating,id_])
        ans.sort(reverse=True)
        return [x[1] for x in ans]





