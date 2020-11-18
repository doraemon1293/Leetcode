from typing import List
import collections


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        smaller = [0] * len(instructions)
        bigger = [0] * len(instructions)
        MOD = 10 ** 9 + 7

        def merge_sort(enums):
            if len(enums) < 2:
                return enums
            else:
                mid = len(enums) // 2
                left = merge_sort(enums[:mid])
                left1 = collections.deque(left)
                right = merge_sort(enums[mid:])
                right1 = collections.deque(right)
                res = []
                while left and right:
                    if right[-1][1] > left[-1][1]:
                        smaller[right[-1][0]] += len(left)
                        res.append(right.pop())
                    else:
                        res.append(left.pop())

                left = left1
                right = right1
                res = []
                while left and right:
                    if right[0][1] < left[0][1]:
                        bigger[right[0][0]] += len(left)
                        res.append(right.popleft())
                    else:
                        res.append(left.popleft())
                if left:
                    res += left
                elif right:
                    res += right
                return res

        merge_sort(list(enumerate(instructions)))
        ans = 0
        for a, b in zip(smaller, bigger):
            ans = (ans + min(a, b)) % MOD
        return ans


print(Solution().createSortedArray([1, 3, 3, 3, 2, 4, 2, 1, 2]))
