from collections import deque


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """

        def get_candidates(arr):
            res = set()
            for s in arr:
                for temp in bank:
                    if len(temp) == len(s) and temp not in visited:
                        diff = 0
                        for i in range(len(s)):
                            if s[i] != temp[i]:
                                diff += 1
                                if diff > 1:
                                    break
                        if diff == 1:
                            visited.add(temp)
                            res.add(temp)
            return res

        arr = {start}
        visited = {start}
        move = 0
        while arr:
            move += 1
            new_arr = get_candidates(arr)
            if end in new_arr:
                return move
            arr=new_arr
        return -1
