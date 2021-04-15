from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seq = [0] * ((n - 1) * 2 + 1)
        used = set()

        def dfs(i, seq):
            # end condition
            if len(used) == n:
                return True
            if i == len(seq):
                return False
            if seq[i] == 0:
                for x in range(n, 0, -1):
                    if x not in used:
                        if x == 1:
                            seq[i] = 1
                            used.add(x)
                            if dfs(i + 1, seq):
                                return True
                            else:
                                seq[i] = 0
                                used.remove(x)
                        elif (i + x) < len(seq) and seq[i + x] == 0:
                            seq[i] = seq[i + x] = x
                            used.add(x)
                            if dfs(i + 1, seq):
                                return True
                            else:
                                seq[i] = seq[i + x] = 0
                                used.remove(x)
            else:
                if dfs(i + 1, seq):
                    return True
                else:
                    return False

        dfs(0, seq)
        return seq