class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        memo = {}
        n = 0
        ref = sum([2 ** i * cells[i] for i in range(8)])
        memo[ref] = 0
        flag = True
        while n < N:
            n += 1
            cells = [0 if i == 0 or i == 7 else int(cells[i - 1] == cells[i + 1]) for i in range(8)]
            ref = sum([2 ** i * cells[i] for i in range(8)])
            if flag and ref in memo:
                last_n = memo[ref]
                n += ((N - n) // (n - last_n)) * (n - last_n)
                flag = False
            else:
                memo[ref] = n

        return cells


cells = [1, 0, 0, 1, 0, 0, 1, 0]
N = 1000000000
cells = [0, 1, 0, 1, 1, 0, 0, 1]
N = 7
print(Solution().prisonAfterNDays(cells, N))
