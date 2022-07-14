class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def lcd(x, y):
            a, b = x, y
            while a % b:
                a, b = b, a % b
            return b

        stack = [nums[0]]
        for i in range(1, len(nums)):
            stack.append(nums[i])
            while len(stack) >= 2:
                x, y = stack[-1], stack[-2]
                temp = lcd(x, y)
                if temp > 1:
                    stack.pop()
                    stack.pop()
                    stack.append(x * y // temp)
                else:
                    break
        return stack
