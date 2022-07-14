class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        arr = [0]
        mini = maxi = 0
        for d in differences:
            arr.append(arr[-1] + d)
            mini = min(mini, arr[-1])
            maxi = max(maxi, arr[-1])
        arr = [x + (lower - mini) for x in arr]

        if upper >= maxi + (lower - mini):
            return upper - maxi + (lower - mini) + 1
        else:
            return 0
