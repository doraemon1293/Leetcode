# coding=utf-8
'''
Created on 2017å¹?7æœ?24æ—?

@author: Administrator
'''


def designProbTest(functions, parameters):
    for i in xrange(len(functions)):
        f, para = functions[i], parameters[i]
        if f[0].isupper():
            cls = eval(f + "(*para)")
        else:
            print eval("cls." + f + "(*para)")


class Trie(object):
    END = '/'

    def __init__(self):
        self.root = {}

    def add(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.END] = None

    def find_prefix(self, word):  # find the shortest prefix of the word in Trie, if cannot find return word itself
        node = self.root
        res = []
        i = 0
        while i < len(word) and node != None:
            node = node.get(word[i], None)
            i += 1
        return node


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        self.d = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.d[key] = val
        self.trie.add(key)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """

        def get_sum(node, prefix):
            res = 0
            for ch in node:
                if ch == "/":
                    res += self.d[prefix]
                else:
                    res += get_sum(node[ch], prefix + ch)
            return res

        node = self.trie.find_prefix(prefix)
        if node == None:
            return 0
        else:
            return get_sum(node, prefix)


functions = ["MapSum", "insert", "sum", "insert", "sum"]
parameters = [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
designProbTest(functions, parameters)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
