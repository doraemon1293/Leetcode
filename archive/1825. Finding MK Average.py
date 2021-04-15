import collections
class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.stream =collections.deque()

    def addElement(self, num: int) -> None:
        self.stream.append(num)
        if len(self.stream)>self.m:
            self.stream.popleft()

    def calculateMKAverage(self) -> int:
        if len(self.stream)<self.m:
            return -1
        container = sorted(self.stream)[self.k:-self.k]
        return sum(container)//len(container)