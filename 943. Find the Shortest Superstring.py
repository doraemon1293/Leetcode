class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """

        def overlap(s1, s2):
            length = min(len(s1), len(s2))
            for i in range(length - 1, -1, -1):
                if s1[len(s1) - i:] == s2[:i]:
                    return len(s2) - i

        N = len(A)
        dis = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                dis[i][j] = overlap(A[i], A[j])
                dis[j][i] = overlap(A[j], A[i])

        def find_min_distance(start_node, unvisited):
            if (start_node, tuple(unvisited)) in memo:
                return memo[start_node, tuple(unvisited)]
            if len(unvisited) == 0:
                return 0, None

            min_distance = float("inf")
            next_node = None
            for i in range(len(unvisited)):
                new_node = unvisited[i]
                new_unvisited = unvisited[:i] + unvisited[i + 1:]
                distance = find_min_distance(new_node, new_unvisited)[0]
                distance += dis[start_node][new_node]
                if distance < min_distance:
                    min_distance = distance
                    next_node = new_node
            memo[start_node, tuple(unvisited)] = (min_distance, next_node)
            return memo[start_node, tuple(unvisited)]

        memo = {}
        min_length = float("inf")
        min_start_node = None
        for start_node in range(N):
            unvisited = [i for i in range(N) if i != start_node]
            length = len(A[start_node])
            length += find_min_distance(start_node, unvisited)[0]
            if length < min_length:
                min_length = length
                min_start_node = start_node
        path = [min_start_node]
        unvisited = [i for i in range(N) if i != min_start_node]
        node = min_start_node
        ans = A[min_start_node]
        while unvisited:
            next_node = memo[node, tuple(unvisited)][1]
            path.append(next_node)
            unvisited = [unvisited[i] for i in range(len(unvisited)) if unvisited[i] != next_node]
            ans += A[next_node][-dis[node][next_node]:]
            node = next_node
        return ans
        # print(min_start_node, min_length)
        # print(path)
        # print(ans)


A = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
A=["alex","loves","leetcode"]
print(Solution().shortestSuperstring(A))
