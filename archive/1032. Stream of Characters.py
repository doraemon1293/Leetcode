class StreamChecker:

    def __init__(self, words):
        self.trie={}
        self.nodes=[]
        for word in words:
            trie=self.trie
            for ch in word:
                trie.setdefault(ch,{})
                trie=trie[ch]
            trie['#']='#'

    def query(self, letter: str) -> bool:
        self.nodes.append(self.trie)
        self.nodes=[node[letter] for node in self.nodes if letter in node]
        for node in self.nodes:
            if '#' in node:
                return True
        return False
words=["c","cd","cde","f","kl"]
obj=StreamChecker(words)




# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)