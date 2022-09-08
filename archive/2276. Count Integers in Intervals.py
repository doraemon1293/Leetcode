import sortedcontainers

class CountIntervals:

    def __init__(self):
        self.intervals = sortedcontainers.SortedList()
        self._count = 0

    def add(self, left: int, right: int) -> None:
        ind =self.intervals.bisect_left((left,))
        while ind<len(self.intervals) and self.intervals[ind][0]<=right+1:
            l,r=self.intervals.pop(ind)
            self._count-=r-l+1
            right=max(r,right)
        if ind-1>=0 and self.intervals[ind-1][1]>=left-1:
            l,r=self.intervals.pop(ind-1)
            self._count-=r-l+1
            left=l
            right=max(r,right)
        self.intervals.add((left,right))
        self._count+=right-left+1

    def count(self) -> int:
        return self._count