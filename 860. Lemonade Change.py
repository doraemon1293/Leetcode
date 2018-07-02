class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        from collections import  defaultdict
        d=defaultdict(int)
        for x in bills:
            if x==5:
                d[5]+=1
            if x==10:
                if d[5]==0:
                    return False
                d[5]-=1
                d[10]+=1
            if x==20:
                if d[10]==0:
                    if d[5]<3:
                        return False
                    else:
                        d[5]-=3
                else:
                    d[10]-=1
                    if d[5]<1:
                        return False
                    else:
                        d[5]-=1
        return True


