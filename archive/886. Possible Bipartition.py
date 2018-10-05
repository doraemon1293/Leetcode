class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        g=defaultdict(list)
        for u,v in dislikes:
            g[u].append(v)
            g[v].append(u)
        color={}
        def dfs(node,c=0):
            if node in color:
                return color[node]==c
            color[node]=c
            for n_node in g[node]:
                if not dfs(n_node,c^1):
                    return False
            return True

        for node in (1,N+1):
            if node not in color:
                if not dfs(node):
                    return False
        return True


N = 3
dislikes = [[1, 2], [1, 3], [2, 3]]
print(Solution().possibleBipartition(N, dislikes))
