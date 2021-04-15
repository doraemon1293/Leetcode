class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        root = self.root
        for ch in word:
            root.setdefault(ch, {})
            root = root[ch]
        root.setdefault(None, 0)
        root[None] += 1

    def countWordsEqualTo(self, word: str) -> int:
        root = self.root
        for ch in word:
            if ch not in root:
                return 0
            root = root[ch]
        return root.get(None, 0)

    def countWordsStartingWith(self, prefix: str) -> int:
        def dfs(root):
            res = root.get(None, 0)
            for ch in root:
                if ch != None:
                    res += dfs(root[ch])
            return res

        root = self.root
        for ch in prefix:
            if ch not in root:
                return 0
            root = root[ch]
        return dfs(root)

    def erase(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch not in root:
                return
            root = root[ch]
        if root.get(None, 0):
            root[None] -= 1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)