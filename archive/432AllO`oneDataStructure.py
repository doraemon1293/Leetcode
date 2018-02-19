# coding=utf-8
'''
Created on 2017å¹?9æœ?19æ—?

@author: Administrator
'''


class LinkedNode(object):

    def __init__(self, v, key):
        self.left = None
        self.right = None
        self.keys = set([key])
        self.v = v


class LinkedSet(object):

    def __init__(self):
        self.head = LinkedNode(-float("inf"), "")
        self.tail = LinkedNode(float("inf"), "")
        self.head.right = self.tail
        self.tail.left = self.head

    def insertOnLeft(self, node, new_node):
        left_node = node.left
        left_node.right = new_node
        new_node.left = left_node
        new_node.right = node
        node.left = new_node

    def insertOnRight(self, node, new_node):
        right_node = node.right
        node.right = new_node
        new_node.left = node
        new_node.right = right_node
        right_node.left = new_node

    def remove(self, node):
        left_node, right_node = node.left, node.right
        left_node.right = right_node
        right_node.left = left_node


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}  # keys->nodes
        self.linkedSet = LinkedSet()

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.d:
            node = self.d[key]
            if node.right.v == node.v + 1:
                node.keys.remove(key)
                node.right.keys.add(key)
                self.d[key] = node.right
                if len(node.keys) == 0:
                    self.linkedSet.remove(node)
            else:
                node.keys.remove(key)
                new_node = LinkedNode(node.v + 1, key)
                self.linkedSet.insertOnRight(node, new_node)
                self.d[key] = new_node
                if len(node.keys) == 0:
                    self.linkedSet.remove(node)
        else:
            if self.linkedSet.head.right.v == 1:
                self.linkedSet.head.right.keys.add(key)
                self.d[key] = self.linkedSet.head.right
            else:
                new_node = LinkedNode(1, key)
                self.linkedSet.insertOnRight(self.linkedSet.head, new_node)
                self.d[key] = new_node
        # print key, self.d[key].keys, self.d[key].v

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.d:
            node = self.d[key]
            if node.v == 1:
                node.keys.remove(key)
                del self.d[key]
                if len(node.keys) == 0:
                    self.linkedSet.remove(node)
            else:
                if node.left.v == node.v - 1:
                    node.keys.remove(key)
                    node.left.keys.add(key)
                    self.d[key] = node.left
                    if len(node.keys) == 0:
                        self.linkedSet.remove(node)
                else:
                    node.keys.remove(key)
                    new_node = LinkedNode(node.v - 1, key)
                    self.linkedSet.insertOnLeft(node, new_node)
                    self.d[key] = new_node
                    if len(node.keys) == 0:
                        self.linkedSet.remove(node)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        node = self.linkedSet.tail.left
        res = node.keys.pop()
        node.keys.add(res)
        return res

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        node = self.linkedSet.head.right
        res = node.keys.pop()
        node.keys.add(res)
        return res


def designProbTest(functions, parameters):
    for i in xrange(len(functions)):
        f, para = functions[i], parameters[i]
        if f[0].isupper():
            cls = eval(f + "(*para)")
        else:
            print eval("cls." + f + "(*para)")


functions = ["AllOne", "inc", "inc", "inc", "inc", "inc", "inc", "inc", "inc", "inc", "inc", "inc", "inc", "getMinKey"]
parameters = [[], ["a"], ["b"], ["c"], ["d"], ["a"], ["b"], ["c"], ["d"], ["c"], ["d"], ["d"], ["a"], []]

designProbTest(functions, parameters)
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
