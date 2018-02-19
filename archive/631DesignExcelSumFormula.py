# coding=utf-8
'''
Created on 2017å¹?8æœ?9æ—?

@author: Administrator
'''


class Excel(object):

    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        self.arr = [[0] * (ord(W) - ord('A') + 1) for _ in xrange(H)]

    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        self.arr[r - 1][ord(c) - ord("A")] = v

    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        if type(self.arr[r - 1][ord(c) - ord("A")]) == int:
            return self.arr[r - 1][ord(c) - ord("A")]
        else:
            return self.parse(self.arr[r - 1][ord(c) - ord("A")])

    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        self.arr[r - 1][ord(c) - ord("A")] = strs
        return self.parse(strs)

    def parse(self, strs):
        val = 0
        for s in strs:
            if ":" in s:
                c1 = s.split(":")[0][0]
                r1 = int(s.split(":")[0][1:])
                c2 = s.split(":")[1][0]
                r2 = int(s.split(":")[1][1:])
                for c in xrange(ord(c1), ord(c2) + 1):
                    c = chr(c)
                    for r in xrange(r1, r2 + 1):
                        val += self.get(r, c)
            else:
                c = s[0]
                r = int(s[1:])
                val += self.get(r, c)
        return val


functions = ["Excel", "get", "set", "get", "sum", "set", "get", "sum", "set", "get"]
parameters = [[5, "E"], [1, "A"], [1, "A", 1], [1, "A"], [2, "B", ["A1", "A1"]], [1, "A", 2], [2, "B"], [3, "C", ["B2", "A1:B2"]], [2, "B", 0], [3, "C"]]

for i in xrange(len(functions)):
    f, para = functions[i], parameters[i]
    if f[0].isupper():
        cls = eval(f + "(*para)")
    else:
        print eval("cls." + f + "(*para)")

# print excel.sum(1, "A", ["A2"])
# print excel.set(2, "A", 1)
# print excel.get(1, "A")

# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)
