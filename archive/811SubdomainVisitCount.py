class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        d = defaultdict(int)
        for cpdomains in cpdomains:
            count, domain = cpdomains.split(" ")
            count = int(count)
            dom = []
            for s in domain.split(".")[::-1]:
                dom.append(s)
                d[tuple(dom)] += count
        return [str(v) + " " + ".".join(k[::-1]) for k, v in d.items()]


cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(Solution().subdomainVisits(cpdomains))
