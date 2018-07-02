class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        d=defaultdict(set)
        for x,y in richer:
            d[y].add(x)
        ans=[None]*len(quiet)

        def solve(x):
            if ans[x] is not None:
                return ans[x]
            mini=quiet[x]
            person=x
            for y in d[x]:
                temp_quiet,temp_person=solve(y)
                if temp_quiet<mini:
                    mini=temp_quiet
                    person=temp_person
            ans[x]=(mini,person)
            return (mini,person)
        for i in range(len(quiet)):
            solve(i)
        ans=[x[1] for x in ans]
        return ans