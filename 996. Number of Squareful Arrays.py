from collections import Counter


class Solution:
    def numSquarefulPerms(self, A: 'List[int]') -> 'int':
        if len(A) == 1:
            return 1
        self.ans = 0
        perfect_squares = {x ** 2 for x in range(31623)}
        remains = Counter(A)

        def dfs(arr, remains):
            if len(arr) == len(A):
                self.ans += 1
            else:
                for a in remains:
                    if (len(arr) == 0 or arr[-1] + a in perfect_squares) and remains[a] > 0:
                        arr.append(a)
                        remains[a] -= 1
                        dfs(arr, remains)
                        arr.pop()
                        remains[a] += 1

        dfs([], remains)
        return self.ans
