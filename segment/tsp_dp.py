# tsp问题
class Solution:
    def __init__(self, X, start_node):
        self.X = X  # 距离矩阵
        self.start_node = start_node  # 开始的节点
        self.memo = {}  # memorise status

    # tsp总接口
    def tsp(self):
        unvisited = tuple([i for i in range(len(self.X)) if i != self.start_node])
        return self.solve(self.start_node, unvisited)  # 求解函数

    def solve(self, start_node, unvisited):
        if (start_node, unvisited) in self.memo:
            return self.memo[start_node, unvisited][0]
        if len(unvisited) == 0:
            self.memo[start_node, unvisited] = (self.X[start_node][self.start_node], self.start_node)
            return self.X[start_node][self.start_node]
        min_distance = float("inf")
        next_node = None
        for i in range(len(unvisited)):
            node = unvisited[i]
            new_unvisited = unvisited[:i] + unvisited[i + 1:]
            distance = self.solve(node, new_unvisited)
            distance += self.X[start_node][node]
            if distance < min_distance:
                min_distance = distance
                next_node = node
        self.memo[start_node, unvisited] = (min_distance, next_node)
        return min_distance


D = [[-1, 10, 20, 30, 40, 50], [12, -1, 18, 30, 25, 21], [23, 19, -1, 5, 10, 15], [34, 32, 4, -1, 8, 16],
     [45, 27, 11, 10, -1, 18], [56, 22, 16, 20, 12, -1]]
start_node = 0
S = Solution(D, start_node)
print(S.tsp())
path = [start_node]
node = start_node
unvisited = [i for i in range(len(D)) if i != start_node]
while unvisited:
    next_node = S.memo[node, tuple(unvisited)][1]
    path.append(next_node)
    unvisited.pop(unvisited.index(next_node))
    node = next_node
print(path)
