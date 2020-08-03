from collections import Counter
import bisect


class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        counter = Counter(A)
        keys = sorted(list(counter.keys()))
        ans = 0
        MOD = 10 ** 9 + 7
        for i in range(len(keys)):
            a1 = keys[i]
            for j in range(i, len(keys)):
                a2 = keys[j]
                a3 = target - a2 - a1
                if a3 >= a2:
                    if a3 in counter:
                        n1, n2, n3 = counter[a1], counter[a2], counter[a3]
                        if a1 == a2 == a3:
                            ans = (ans + n1 * (n1 - 1) * (n1 - 2) // 6) % MOD
                        elif a1 == a2:
                            ans = (ans + n1 * (n1 - 1) // 2 * n3) % MOD
                        elif a2 == a3:
                            ans = (ans + n1 * n2 * (n2 - 1) // 2) % MOD
                        else:
                            ans = (ans + n1 * n2 * n3) % MOD
                else:
                    break
        return ans


A = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
target = 8
print(Solution().threeSumMulti(A, target))
