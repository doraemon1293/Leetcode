class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S==T: return 0
        from collections import defaultdict
        from collections import deque
        d=defaultdict(set)
        for i,route in enumerate(routes):
            for stop in route:
                d[stop].add(i)
        visited={S}
        q=deque([(S,0)])
        while q:
            stop,transfer=q.popleft()
            if stop==T:
                return transfer
            for bus in d[stop]:
                for stop1 in routes[bus]:
                    if stop1 not in visited:
                        visited.add(stop1)
                        q.append((stop1,transfer+1))
                routes[bus]=[]
        return -1







routes=[[25,33],[3,5,13,22,23,29,37,45,49],[15,16,41,47],[5,11,17,23,33],[10,11,12,29,30,39,45],[2,5,23,24,33],[1,2,9,19,20,21,23,32,34,44],[7,18,23,24],[1,2,7,27,36,44],[7,14,33]]
S=7
T=47
print(Solution().numBusesToDestination(routes,S,T))







