class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        p1 = 0
        d = {}
        for piece in pieces:
            d[piece[0]] = piece

        while p1 < len(arr):
            if arr[p1] in d:
                piece = d[arr[p1]]
                length = min(len(piece), len(arr) - p1)
                if arr[p1:p1 + length] == piece[:length]:
                    p1 += length
                else:
                    return False

            else:
                return False
        return True




