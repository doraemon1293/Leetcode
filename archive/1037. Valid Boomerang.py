class Solution:
    def isBoomerang(self, points) -> bool:
        a,b,c=points


        return not (c[1]-b[1])*(b[0]-a[0])==(b[1]-a[1])*(c[0]-b[0])
