class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        def find_min_index(arr):
            min_value = float("inf")
            min_index = None
            for i, x in enumerate(arr):
                if x < min_value:
                    min_value = x
                    min_index = i
            return min_index
        summ=sum(a)
        for _ in range(K):
            min_index=find_min_index(A)
            summ -= 2 * A[min_index]
            A[min_index]*=-1
        return summ

