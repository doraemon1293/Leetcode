class Solution:
    def maxStudents(self, seats: list) -> int:
        dp = {0: 0}

        M, N = len(seats), len(seats[0])

        def legal(mask, last_mask):
            for col in range(N):
                if (mask >> col)&1:

                    if col - 1 >= 0 and ((last_mask >> (col - 1)) & 1):
                        return False
                    if col + 1 < N and ((last_mask >> (col + 1)) & 1):
                        return False
            return True


        def dfs(cur_row, col, people_mask, people_number):
            if col >= N:
                self.people_masks[people_mask] = people_number
            else:
                while col < N and seats[cur_row][col] == '#':
                    col += 1
                if col == N:
                    self.people_masks[people_mask] = people_number
                else:
                    # 找到一个座位
                    # 1 不坐这个座位
                    dfs(cur_row, col + 1, people_mask, people_number)
                    # 2 坐这个座位
                    dfs(cur_row, col + 2, people_mask | (1 << col), people_number + 1)

        for row in range(M):
            new_dp = {}
            self.people_masks = {}
            dfs(row, 0, 0, 0)
            for mask in self.people_masks:
                for last_mask in dp:
                    if legal(mask, last_mask):
                        new_dp[mask] = max(new_dp.get(mask, 0), dp[last_mask] + self.people_masks[mask])
            dp = new_dp
        return max(dp.values())