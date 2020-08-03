class Solution:
    def isSolvable(self, words: list, result: str) -> bool:
        maxi = max(len(word) for word in words)
        if len(result) < maxi:
            return False
        d = {}
        numbers = set(range(0, 10))
        words = words + [result]
        words = [word[::-1] for word in words]
        cannot_be_zero = set([word[-1] for word in words])
        max_col = max([len(word) for word in words])

        def dfs(i, j, summ):
            if j == max_col:
                return summ == 0
            if i == len(words) - 1:
                if words[i][j] in d:
                    if d[words[i][j]] == summ % 10:
                        return dfs(0, j + 1, summ // 10)
                    else:
                        return False
                else:
                    if summ % 10 not in numbers or (summ % 10 == 0 and words[i][j] in cannot_be_zero):
                        return False
                    else:
                        d[words[i][j]] = summ % 10
                        numbers.remove(summ % 10)
                        if dfs(0, j + 1, summ // 10):
                            return True

                        del d[words[i][j]]
                        numbers.add(summ % 10)
            else:
                if j >= len(words[i]):
                    return dfs(i + 1, j, summ)
                else:
                    if words[i][j] in d:
                        summ += d[words[i][j]]
                        return dfs(i+1,j,summ)
                    else:
                        for x in (range(1, 10) if words[i][j] in cannot_be_zero else range(0,10)):
                            if x in numbers:
                                d[words[i][j]] = x
                                numbers.remove(x)
                                if dfs(i + 1, j, summ + x):
                                    return True
                                else:
                                    del d[words[i][j]]
                                    numbers.add(x)
                        return False

        ans= dfs(0, 0, 0)
        print(d)
        return ans


words = ["AA", "BB"]
result = "CC"
# words = ["SEND", "MORE"]
# result = "MONEY"
print(Solution().isSolvable(words, result))
