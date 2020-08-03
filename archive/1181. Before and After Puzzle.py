import collections


class Solution:
    def beforeAndAfterPuzzles(self, phrases: list) -> list:
        before = collections.defaultdict(list)
        after = collections.defaultdict(list)
        for i, p in enumerate(phrases):
            before[p.split(" ")[0]].append(i)
            after[p.split(" ")[-1]].append(i)
        ans = set()
        for k in after:
            for i in after[k]:
                for j in before[k]:
                    if i != j:
                        a = phrases[i]
                        b = phrases[j]
                        ans.add(a+ (b[b.find(" "):] if b.find(" ")!=-1 else ""))
        return sorted(list(ans))


phrases = ["writing code", "code rocks"]
print(Solution().beforeAndAfterPuzzles(phrases))
