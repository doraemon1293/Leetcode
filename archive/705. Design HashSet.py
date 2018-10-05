class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.cap = 10000
        self.set = [[] for _ in range(10000)]

    def hash(self, key):
        return key % self.cap

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.contain(key):
            return
        else:
            v = self.hash(key)
            if self.set[v].append(key):
                return
            else:
                self.double_cap()

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
