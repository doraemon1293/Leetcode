class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def get_count(s):
            res=[0]*52
            for i in range(len(s)):
                if i%2==0:
                    res[ord(s[i])-ord("a")]+=1
                else:
                    res[ord(s[i]) - ord("a")+26] += 1
            return tuple(res)
        d={}
        for s in A:
            k=get_count()
            d.setdefault(k,[])
            d[k].append(s)
        return len(d)




