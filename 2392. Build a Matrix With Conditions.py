from typing import List
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_edge={}
        for i in range(1,k+1):
            row_edge[i]=set()
        col_edge={}
        for i in range(1,k+1):
            col_edge[i]=set()

        for s,t in rowConditions:
            row_edge[s].add(t)
        for s, t in colConditions:
            col_edge[s].add(t)

        def top_sort(edges):
            indegree={}
            for i in range(1,k+1):
                indegree[i]=0

            for i in range(1,k+1):
                for t in edges[i]:
                    indegree[t]+=1

            zeros=[i for i in range(1,k+1) if indegree[i]==0 ]
            res=zeros
            while zeros:
                new_zeros=[]
                for v0 in zeros:
                    for v1 in edges[v0]:
                        indegree[v1]-=1
                        if indegree[v1]==0:
                            new_zeros.append(v1)
                zeros=new_zeros
                res += zeros
            if len(res)==k:
                return res
            else:
                return []
        row_top_sort=top_sort(row_edge)
        col_top_sort=top_sort(col_edge)
        if row_top_sort and col_top_sort:
            coord={}
            for i in range(1,k+1):
                coord[i]=[None,None]
            for row,i in enumerate(row_top_sort):
                coord[i][0]=row
            for col,i in enumerate(col_top_sort):
                coord[i][1]=col
            matrix=[[0]*k for _ in range(k)]
            for i in coord:
                matrix[coord[i][0]][coord[i][1]]=i
            return matrix


        else:
            return []