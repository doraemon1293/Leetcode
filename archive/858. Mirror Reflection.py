class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        targets=[(p,0),(p,p),(0,p)]
        from fractions import Fraction
        x,y=0,0
        dx,dy=p,q
        while True:
            t=min([temp for temp in (Fraction(-x,dx),Fraction(p-x,dx),Fraction(-y,dy),Fraction(p-y,dy)) if temp>0])
            x,y=x+dx*t,y+dy*t
            if (x,y) in targets:
                return targets.index((x,y))
            else:
                if x==p or x==0:
                    dx=-dx
                else:
                    dy=-dy
