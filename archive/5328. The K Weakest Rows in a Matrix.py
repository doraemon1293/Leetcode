class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return  sorted([(sum(a),i) for i,a in enumerate(mat)])[:k]

