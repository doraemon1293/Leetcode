import collections


class Solution:
    def generateSentences(self, synonyms: list, text: str) -> list:
        uf = {}

        def find(a):
            uf.setdefault(a, a)
            path = []
            while uf[a] != a:
                path.append(a)
                a = uf[a]
            for x in path:
                uf[x] = a
            return a

        def connect(a, b):
            uf[find(a)] = find(b)

        for a, b in synonyms:
            connect(a, b)

        syn = collections.defaultdict(set)
        for k in uf:
            syn[find(k)].add(k)
        text = text.split(" ")
        ans=[[]]
        for word in text:
            words=syn[find(word)] if word in uf else [word]
            ans=[a+[b] for a in ans for b in words]
        ans=[" ".join(arr) for arr in ans]
        ans.sort()
        return ans


synonyms=[["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
text="I am happy today but was sad yesterday"
print(Solution().generateSentences(synonyms,text))