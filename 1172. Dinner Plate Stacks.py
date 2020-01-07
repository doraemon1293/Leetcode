import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.heap = []

    def push(self, val: int) -> None:
        while self.heap and (self.heap[0] >= len(self.stacks) or len(self.stacks[self.heap[0]]) >= self.capacity):
            heapq.heappop(self.heap)
        if self.heap:
            i = self.heap[0]
            self.stacks[i].append(val)
            if len(self.stacks[i]) == self.capacity:
                heapq.heappop(self.heap)
        else:
            self.stacks.append([val])
            if self.capacity != 1:
                heapq.heappush(self.heap, len(self.stacks) - 1)

    def pop(self) -> int:
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stacks):
            if self.stacks[index]:
                res = self.stacks[index].pop()
                while self.stacks and self.stacks[-1] == []:
                    self.stacks.pop()
                if index < len(self.stacks):
                    heapq.heappush(self.heap, index)
                return res
            else:
                return -1
        else:
            return -1

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
