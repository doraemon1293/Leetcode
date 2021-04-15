import collections


class FrontMiddleBackQueue:

    def __init__(self):
        self.front = collections.deque()
        self.back = collections.deque()

    def rebalance(self):
        while len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        while len(self.back) > len(self.front) + 1:
            self.front.append(self.back.popleft())

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val: int) -> None:
        self.front.append(val)
        self.rebalance()

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self.rebalance()

    def popFront(self) -> int:
        if len(self.front) + len(self.back) == 0:
            return -1
        if self.front:
            res = self.front.popleft()
        else:
            res=self.back.popleft()
        self.rebalance()

        return res

    def popMiddle(self) -> int:
        if len(self.front) + len(self.back) == 0:
            return -1
        if len(self.front)==len(self.back):
            res = self.front.pop()
        else:
            res=self.back.popleft()
        self.rebalance()
        return res

    def popBack(self) -> int:
        if len(self.front) + len(self.back) == 0:
            return -1
        res = self.back.pop()

        self.rebalance()

        return res

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
