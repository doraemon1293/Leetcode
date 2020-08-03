class Solution:
    def removeCoveredIntervals(self, intervals: list) -> int:
        intervals.sort(key=lambda x:x[0])
        right=intervals[0][1]
        removed=0
        for i in range(1,len(intervals)):
            interval=intervals[i]
            if right >=interval[1]:
                removed+=1
            else:
                right=interval[1]
        return len(intervals)-removed
