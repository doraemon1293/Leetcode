from collections import Counter


class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0: return 0
        c = Counter(A)
        unique_numbers_set = set(A)
        unique_numbers = sorted(unique_numbers_set)
        mini = unique_numbers[0]

        def find_next_avail(mini):
            while mini in unique_numbers_set:
                mini += 1
            unique_numbers_set.add(mini)
            return mini

        ans = 0
        for num in unique_numbers:
            for _ in range(c[num] - 1):
                mini = find_next_avail(max(mini, num))
                ans += mini - num
        return ans
