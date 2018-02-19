# coding=utf-8
'''
Created on 2017å¹?8æœ?18æ—?

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

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        if word == "":
            node[None] = None
        for ch in word:
            node = node.setdefault(ch, {})
        node[None] = None

    def fuzzySearch(self, word):
        nodes = [self.root]
        for ch in word:
            if nodes == []:
                return False
            if ch == ".":
                newNodes = []
                for node in nodes:
                    for k in node:
                        if k != None:
                            newNodes.append(node[k])
                nodes = newNodes
            else:
                nodes = [node[ch] for node in nodes if ch in node]
        for node in nodes:
            if None in node:
                return True
        return False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.addWord(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.trie.fuzzySearch(word)


WordDictionary()
functions = ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
parameters = [[], ["abc"], ["abd"], ["acb"], ["b.."], ["a.."], ["abc"], ["b.."]]

functions = ["WordDictionary", "addWord", "addWord", "search", "search", "search", "search", "search", "search"]
parameters = [[], ["a"], ["b"], ["."], ["a"], ["aa"], ["a"], [".a"], ["a."]]

# functions = ["WordDictionary", "addWord", "addWord", "addWord", "search"]
# parameters = [[], ["a"], ["b"], ["c"], ["."]]
designProbTest(functions, parameters)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
