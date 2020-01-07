class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        if a+1==b==c-1:
            mini=0
        elif min(b-a,c-b)==1 or min(b-a,c-b)==2
            mini=1
        else:
            mini=2
        maxi=c-a-2
        return [mini,maxi]
