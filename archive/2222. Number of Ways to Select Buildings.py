class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {"0": 0, "01": 0, "1": 0, "10": 0}
        ans = 0
        for ch in s:
            new_counts = counts.copy()
            if ch == "0":
                new_counts["0"] += 1
                new_counts["10"] += counts["1"]
                ans += new_counts["01"]
            else:
                new_counts["1"] += 1
                new_counts["01"] += counts["0"]
                ans += new_counts["10"]
            counts = new_counts
        return ans
