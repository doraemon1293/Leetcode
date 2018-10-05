class Solution:
    def stoneGame(self, piles):
        N = len(piles)
        mem={}
        def dp(i, j):
            if (i,j) in mem: return mem[i,j]
            if i > j: return 0
            parity = (j - i - N) % 2
            if parity == 1:  # first player
                mem[i,j]=max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))

                return mem[i,j]
            else:
                mem[i,j]=min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

                return mem[i,j]

        return dp(0, N - 1) > 0