class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """

        d = {}

        def find(x):
            if x not in d:
                d[x] = x
                return x
            else:
                path = [x]
                while x != d[x]:
                    x = d[x]
                    path.append(x)
                for x1 in path:
                    d[x1] = x
                return x

        def union(x, y):
            d[find(x)] = find(y)

        for a, b in pairs:
            union(a, b)

        arrs = {}
        for k in d:
            v = find(k)
            arrs.setdefault(v, ([], []))
            arrs[v][0].append(s[k])
            arrs[v][1].append(k)
        ans = list(s)
        for arr in arrs.values():
            arr[0].sort()
            arr[1].sort()
            for i in range(len(arr[0])):
                ind = arr[1][i]
                ch = arr[0][i]
                ans[ind] = ch

        return "".join(ans)


s="udyyek"
pairs=[[3,3],[3,0],[5,1],[3,1],[3,4],[3,5]]
print(Solution().smallestStringWithSwaps(s, pairs))
