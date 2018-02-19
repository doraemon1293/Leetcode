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

    def find_prefix(self, prefix):  # find the shortest prefix of the word in Trie, if cannot find return word itself
        node = self.root
        for ch in prefix:
            node = node.get(ch, None)
            if node == None:
                return None
        return node


class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.weights = {}
        for i in xrange(len(words)):
            self.weights[words[i]] = i
        self.prefixTrie = Trie()
        for word in self.weights:
            self.prefixTrie.add(word)
        self.prefixWords = {}
        self.ans = {}

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        if (prefix, suffix) in self.ans:
            return self.ans[(prefix, suffix)]

        def getWordFromNode(cur, node):
            if node == None:
                return []
            res = []
            for ch in node:
                if ch == "/":
                    res.append("".join(cur))
                else:
                    res += getWordFromNode(cur + [ch], node[ch])
            return res

        if prefix in self.prefixWords:
            tempTrie = self.prefixWords[prefix]
        else:
            prefixNode = self.prefixTrie.find_prefix(prefix)
            prefixWords = getWordFromNode(list(prefix), prefixNode)
            tempTrie = Trie()
            self.prefixWords[prefix] = tempTrie
            for word in prefixWords:
                tempTrie.add(word[::-1])
        node = tempTrie.find_prefix(suffix[::-1])
        words = getWordFromNode(list(suffix[::-1]), node)
        # print "prefix", prefix, "suffix", suffix, "prefixWords", prefixWords, "suffixWords", suffixWords, words
        res = -1
        for word in words:
            res = max(res, self.weights[word[::-1]])
        self.ans[(prefix, suffix)] = res
        return res


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# functions = ["WordFilter", "f"]
# parameters = [["apple"], ("a", "e")]
filter = WordFilter(["apple"])
print filter.f("ap", "le")
print filter.f("ap", "le")

print filter.f("b", "")

