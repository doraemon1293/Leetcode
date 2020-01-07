class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        d = {}

        def solve(i, j):
            if i == 0:
                if j == 0:
                    return 1
                else:
                    return 0

            if (i, j) in d:
                return d[i, j]
            d[i, j] = (solve(i - 1, j - 1) * (N - j + 1) + solve(i - 1, j) * max(j - K, 0)) % (10 ** 9 + 7)
            return d[i, j]

        return solve(L, N)