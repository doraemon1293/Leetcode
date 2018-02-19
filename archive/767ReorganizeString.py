class Solution:

    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        from collections import Counter
        counter = Counter(S)
        ans = []
        for _ in range(len(S)):
            temp = counter.most_common()
            if len(ans) == 0 or temp[0][0] != ans[-1]:
                ans.append(temp[0][0])
                counter[temp[0][0]] -= 1
                if counter[temp[0][0]] == 0:
                    del counter[temp[0][0]]
            else:
                if len(temp) == 1:
                    return ""
                else:
                    ans.append(temp[1][0])
                    counter[temp[1][0]] -= 1
                    if counter[temp[1][0]] == 0:
                        del counter[temp[1][0]]
        return "".join(ans)


S = "sdfoisdjfpo"
print(Solution().reorganizeString(S))
