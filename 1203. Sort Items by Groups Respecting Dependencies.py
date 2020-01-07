import collections
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        def top_sort(nodes,rnp):
            in_degree=collections.defaultdict(int)
            out_nodes=collections.defaultdict(set)
            nodes=set(nodes)
            for a,b in rnp:
                if a in nodes and b in nodes:
                    in_degree[b]+=1
                    out_nodes[a].add(b)
            res=[]
            while nodes:
                zero_in_degree_nodes=[node for node in nodes if in_degree[node]==0]
                if zero_in_degree_nodes==[]:
                    return []
                res+=list(zero_in_degree_nodes)
                for node in zero_in_degree_nodes:
                    for t_node in out_nodes[node]:
                        in_degree[t_node]-=1
                nodes=nodes-set(zero_in_degree_nodes)
            return res

        node_group={}
        groups=collections.defaultdict(set)
        groups_rnp=set()
        inner_group_rnp=set()
        for node in range(n):
            node_group[node]=group[node] if group[node]!=-1 else str(node)+"other"
            groups[node_group[node]].add(node)
        for node1 in range(n):
            for node2 in beforeItems[node1]:
                group1=node_group[node1]
                group2=node_group[node2]
                if group1!=group2:
                    groups_rnp.add((group2,group1))
                else:
                    inner_group_rnp.add((node2,node1))
        group_leveorder=top_sort(groups.keys(),groups_rnp)
        if group_leveorder==[]:
            return []

        res=[]
        for group in group_leveorder:
            temp=top_sort(groups[group],inner_group_rnp)
            if temp==[]:
                return []
            else:
                res+=temp
        return res





n=8
m=2
group=[-1,-1,1,0,0,1,0,-1]
beforeItems=[[],[6],[5],[6],[3,6],[],[],[]]
print(Solution().sortItems(n,m,group,beforeItems))



