class Solution:
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        connect_prop = {(" ", " "): {(-1, 0): (0, 0),
                                     (1, 0): (0, 0),
                                     (0, -1): (0, 0),
                                     (0, 1): (0, 0),
                                     },
                        (" ", "/"): {(-1, 0): (0, 1),
                                     (1, 0): (0, 0),
                                     (0, -1): (0, 1),
                                     (0, 1): (0, 0),
                                     },
                        (" ", "\\"): {(-1, 0): (0, 1),
                                      (1, 0): (0, 0),
                                      (0, -1): (0, 0),
                                      (0, 1): (0, 1),
                                      },
                        ("/", " "): {(-1, 0): (0, 0),
                                     (1, 0): (1, 0),
                                     (0, -1): (0, 0),
                                     (0, 1): (1, 0),
                                     },
                        ("/", "/"): {(-1, 0): (0, 1),
                                     (1, 0): (1, 0),
                                     (0, -1): (0, 1),
                                     (0, 1): (1, 0),
                                     },
                        ("/", "\\"): {(-1, 0): (0, 1),
                                      (1, 0): (1, 0),
                                      (0, -1): (0, 0),
                                      (0, 1): (1, 1),
                                      },
                        ("\\", " "): {(-1, 0): (0, 0),
                                      (1, 0): (1, 0),
                                      (0, -1): (1, 0),
                                      (0, 1): (0, 0),
                                      },
                        ("\\", "/"): {(-1, 0): (0, 1),
                                      (1, 0): (1, 0),
                                      (0, -1): (1, 1),
                                      (0, 1): (0, 0),
                                      },
                        ("\\", "\\"): {(-1, 0): (0, 1),
                                       (1, 0): (1, 0),
                                       (0, -1): (1, 0),
                                       (0, 1): (0, 1),
                                       },
                        }
        N = len(grid)
        neighbour = {}

        def connect(x, y):
            if grid[x][y]==" ":
                neighbour.setdefault((x,y,0),set())
            else:
                neighbour.setdefault((x, y, 0), set())
                neighbour.setdefault((x, y, 1), set())
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                tx, ty = x + dx, y + dy
                if 0 <= tx < N and 0 <= ty < N:
                    source = grid[x][y]
                    target = grid[tx][ty]
                    n1, n2 = connect_prop[source, target][dx, dy]
                    neighbour[x, y, n1].add((tx, ty, n2))
                    if (tx,ty,n2)==(1,0,1):
                        print(x,y,dx,dy,n1)

        for x in range(N):
            for y in range(N):
                connect(x, y)
        visited = set()
        ans = 0

        def dfs(node):
            visited.add(node)
            for n_node in neighbour[node]:
                if n_node not in visited:
                    dfs(n_node)

        for node in neighbour:
            if node not in visited:
                ans += 1
                dfs(node)
        return ans


grid = [
  "/\\",
  "\\/"
]
grid=[" /\\"," \\/","\\  "]
print(Solution().regionsBySlashes(grid))
