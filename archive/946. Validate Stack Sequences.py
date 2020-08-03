class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        p = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[p]:
                stack.pop()
                p += 1
        return stack == []


print(Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))
print(Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))
