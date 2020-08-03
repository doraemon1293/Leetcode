class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []

        for ch in s:
            if stack and ch == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])

        ans = []
        for ch, i in stack:
            ans += [ch] * i
        return "".join(ans)
