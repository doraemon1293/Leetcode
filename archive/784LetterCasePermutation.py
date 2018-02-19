# coding=utf-8


class Solution:

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = [""]
        for ch in S:
            if ch.isalpha():
                new_ans = []
                for x in ans:
                    new_ans.append(x + ch.lower())
                    new_ans.append(x + ch.upper())
                ans = new_ans
            else:
                ans = [x + ch for x in ans]
        return ans


S = "a1b2"
# S = ""
print(Solution().letterCasePermutation(S))
