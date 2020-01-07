import bisect


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        d = {}
        for i, ch in enumerate(source):
            d.setdefault(ch, [])
            d[ch].append(i)
        cur_ind = -1
        ans = 1
        for ch in target:
            if ch not in d:
                return -1
            ind = bisect.bisect_right(d[ch], cur_ind)
            while ind == len(d[ch]):
                ans += 1
                cur_ind = -1
                ind = bisect.bisect_right(d[ch], cur_ind)
            cur_ind = d[ch][ind]
        return ans
