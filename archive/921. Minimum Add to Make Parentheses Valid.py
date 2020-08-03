class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        ans = 0
        for ch in S:
            if ch == "(":
                stack.append("(")
            else:
                if stack:
                    stack.pop()
                else:
                    ans += 1
        ans += len(stack)
