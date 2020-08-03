from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        d = {}
        for i, ch in enumerate(s):
            if ch not in d:
                d[ch] = [i, i]
            else:
                d[ch][1] = i

        temp = []
        intervals = list(d.values())
        for st, end in intervals:
            while True:
                new_st, new_end = st, end
                for ch in set(s[st + 1:end]):
                    new_st = min(new_st, d[ch][0])
                    new_end = max(new_end, d[ch][1])
                if new_st == st and new_end == end:
                    break
                st, end = new_st, new_end
            temp.append((end - st + 1, st, end))
        intervals = sorted(temp)
        # print(intervals)
        ans = []
        while intervals:
            st, end = intervals[0][1], intervals[0][2]
            ans.append(s[st:end + 1])
            intervals = [x for x in intervals if x[1] > end or x[2] < st]
            # print(arr)
        return ans


s = "adefcaddaccc"
# s = "abab"
print(Solution().maxNumOfSubstrings(s))
