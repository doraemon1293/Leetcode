class Solution:
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict,deque
        nodes=defaultdict(set)
        for s,t in edges:
            nodes[s].add(t)
            nodes[t].add(s)

        ans=[None]*N
        childs=defaultdict(set)
        count={}
        visited={0}
        stack=[0]
        summ=0
        depth=0
        while stack:
            new_stack=[]
            depth+=1
            for a in stack:
                for b in nodes[a]:
                    if b not in visited:
                        childs[a].add(b)
                        new_stack.append(b)
                        visited.add(b)
                        summ+=depth
            stack=new_stack
        ans[0]=summ

        def get_count_of_nodes(node):
            res=1
            for a in childs[node]:
                res+=get_count_of_nodes(a)
            count[node]=res
            return res
        get_count_of_nodes(0)

        stack=deque([0])
        while stack:
            node=stack.popleft()
            for child in childs[node]:
                ans[child]=ans[node]+(N-2*count[child])
                stack.append(child)
        return ans

N=6
edges=[[0,1],[0,2],[2,3],[2,4],[2,5]]

print(Solution().sumOfDistancesInTree(N,edges))


