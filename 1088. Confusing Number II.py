import bisect
class Solution:
    def confusingNumberII(self, N: int) -> int:
        q = nums = ["0", "1", "6", "8", "9"]

        d = {"1": "1", "6": "9", "8": "8", "9": "6", "0": "0"}

        def is_valid(n):
            for i in range(len(n) // 2 + 1):
                if d[n[i]] != n[-(i + 1)]:
                    return True
            return False

        length = len(str(N))
        if length == 10:
            length = 9
            ans=1
            N=999999999
        else:
            ans=0
        for _ in range(length - 1):
            q = [j + i for j in q for i in nums]
        ind=bisect.bisect_right(q,str(N).zfill(length))
        q = [num.lstrip("0") for num in q[1:ind]]
        for num in q:
            if is_valid(num):
                ans += 1
        return ans


N =1000000000
print(Solution().confusingNumberII(N))
