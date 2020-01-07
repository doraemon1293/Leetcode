class Solution:
    def minHeightShelves(self, books: list, shelf_width: int) -> int:
        dp = [float("inf")] * (len(books)+1)
        dp[0] = 0
        for i in range(len(books)):
            width = books[i][0]
            ind = i
            max_height = books[i][1]
            while ind >= 0 and width <= shelf_width:
                dp[i+1] = min(dp[i+1], dp[ind] + max_height)
                ind -= 1
                width += books[ind][0]
                max_height = max(max_height, books[ind][1])
        return dp[-1]

books = [[1, 7], [6, 4], [10, 7], [6, 10], [8, 10], [1, 10], [10, 7]]
shelf_width = 10
print(Solution().minHeightShelves(books, shelf_width))
