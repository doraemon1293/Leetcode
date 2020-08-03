from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        i = 0
        while i < len(arr):
            j = i
            if i > 0 and arr[i - 1] < arr[i]:
                win = 1
            else:
                win = 0

            while win<k and j + 1 < len(arr) and arr[j + 1] < arr[i]:
                j += 1
                win += 1
            if win == k:
                return arr[i]
            i = j + 1
        return max(arr)