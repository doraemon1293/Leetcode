class Solution:
    def movesToStamp(self, stamp, target):
        def can_be_covered(target):
            if all([ch == "?" for ch in target]):
                return False
            for c1, c2 in zip(target, stamp):
                if c1 != "?" and c1 != c2:
                    return False
            return True

        root = "?" * len(target)
        ans = []
        moves = 0
        max_moves = 10 * len(target)
        while moves < max_moves:
            flag = False
            for i in range(len(target) - len(stamp) + 1):
                s = target[i:i + len(stamp)]
                if can_be_covered(s):
                    target = target[:i - 1] + "?" * len(stamp) + target[i + len(stamp)]
                    moves += 1
                    arr.append(i)
                    flag = True
            if target == root:
                return arr[::-1]
            if flag == False:
                return []
        return []


stamp = "abca"
target = "aabcaca"
print(Solution().movesToStamp(stamp, target))
