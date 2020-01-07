import collections


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = collections.Counter(tiles)
        ans = set()

        def dfs(pre_s):
            for ch in counter:
                if counter[ch]:
                    temp = pre_s + ch
                    counter[ch] -= 1
                    if temp not in ans:
                        ans.add(temp)
                        dfs(temp)
                    counter[ch] += 1
        dfs("")
        return len(ans)


tiles = "SKV"
print(Solution().numTilePossibilities(tiles))
