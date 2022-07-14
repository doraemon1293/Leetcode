import functools
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        @functools.lru_cache(None)
        def dp(i,k):
            if i<0:
                return 0
            #not cover
            not_cover=dp(i-1,k)+(floor[i]=="1")
            #cover
            cover=dp(i-carpetLen,k-1) if k>0 else float("inf")
            return min(not_cover,cover)
        return dp(len(floor)-1,numCarpets)