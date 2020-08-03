class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # a==b <=>a^b==0
        ans = 0
        for i in range(len(arr)):
            temp = arr[i]
            for k in range(i + 1, len(arr)):
                temp ^= arr[k]
                if temp == 0:
                    ans += k - i
        return ans
