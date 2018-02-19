class Solution:

    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        intervals = []
        for i in range(26):
            ch = chr(ord("a") + i)
            l, r = S.find(ch), S.rfind(ch)
            if l != -1 and r != -1:
                intervals.append((l, r))
        intervals.sort()
        print(intervals)
        ind = 0
        while ind < len(intervals) - 1:
            if intervals[ind + 1][0] <= intervals[ind][1]:
                intervals[ind] = (intervals[ind][0], max(intervals[ind][1], intervals[ind + 1][1]))
                del intervals[ind + 1]
            else:
                ind += 1
        print(intervals)
        ans = [x[1] - x[0] + 1 for x in intervals]
        return ans


S = "ababcbacadefegdehijhklij"
S = "abcdefg"
print(Solution().partitionLabels(S))
