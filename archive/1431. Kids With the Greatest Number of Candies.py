class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [c + extraCandies >= max(candies) for i, c in enumerate(candies)]