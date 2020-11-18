class OrderedStream:

    def __init__(self, n: int):
        self.d = {}
        self.p = 1

    def insert(self, id: int, value: str) -> List[str]:
        self.d[id] = value
        res = []
        if id == self.p:
            while self.p in self.d:
                res.append(self.d[self.p])
                self.p += 1
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)