from collections import defaultdict


class DSU:
    def __init__(self):
        self.weights = {}
        self.parents = {}

    def find(self, x):
        if x not in self.parents:
            self.parents[x] = x
            self.weights[x] = 1
            return x
        else:
            path = [x]
            while self.parents[path[-1]] != path[-1]:
                path.append(self.parents[path[-1]])
            root = path[-1]
            for node in path:
                self.parents[node] = root
            return root

    def union(self, elements):
        roots = [self.find(e) for e in elements]
        heaviest_root = max([(self.weights[root], root) for root in roots])[1]
        for root in roots:
            if root != heaviest_root:
                self.weights[heaviest_root] += self.weights[root]
                self.parents[root] = heaviest_root


class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        primes = defaultdict(set)
        for a in A:
            prime = 2
            temp_a=a
            while prime ** 2 <= temp_a:
                while temp_a % prime == 0:
                    primes[prime].add(a)
                    temp_a //= prime
                prime += 1
            if temp_a > 1:
                primes[temp_a].add(a)

        dsu = DSU()
        for s in primes.values():
            dsu.union(s)
        return max(dsu.weights.values())


A = [99, 68, 70, 77, 35, 52, 53, 25, 62]
A = [4, 6, 15, 35]
print(Solution().largestComponentSize(A))
