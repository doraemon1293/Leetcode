from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            mat=[list(row[::-1]) for row in zip(*mat)]

            # for row in mat:
            #     print(row)
            # for row in target:
            #     print(row)


            if mat==target:
                return True
        return False