import collections
import bisect
import random


# Boyer–Moore majority vote algorithm TLE
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr=arr
        self.inds = collections.defaultdict(list)
        for i, num in enumerate(arr):
            self.inds[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        count, major = 0, 0
        for n in self.arr:
            if count == 0:
                major = n
            if major == n:
                count += 1
            else:
                count -= 1
        l_ind = bisect.bisect_left(self.inds[major], left)
        r_ind = bisect.bisect_right(self.inds[major], right)
        if r_ind - l_ind >= threshold:
            return major
        else:
            return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)


# random pick

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.inds = collections.defaultdict(list)
        for i, num in enumerate(arr):
            self.inds[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(10):
            major = self.arr[random.randint(left, right)]
            l_ind = bisect.bisect_left(self.inds[major], left)
            r_ind = bisect.bisect_right(self.inds[major], right)
            if r_ind - l_ind >= threshold:
                return major
        return -1
