class Solution:
    def earliestAcq(self, logs: list, N: int) -> int:
        root = list(range(N))
        self.number = N
        logs.sort()

        def find(i):
            path = []
            temp = i
            while temp != root[temp]:
                temp = root[temp]
                path.append(temp)
            for x in path:
                root[x] = temp
            return temp

        def connect(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                self.number -= 1
                root[root_i] = root[root_j]

        for ts, i, j in logs:
            connect(i, j)
            if self.number == 1:
                return ts
        return -1
