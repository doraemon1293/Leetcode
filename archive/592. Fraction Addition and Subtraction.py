import re


class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """

        def gcd(a, b):
            while a % b:
                a, b = b, a % b
            return b

        def add(a, b, c, d):
            x = a * d + b * c
            y = b * d
            if x == 0:
                return (0, 1)
            temp = gcd(x, y)
            return (x // temp, y // temp)

        nums = [x for x in re.split("[+-]", expression) if x]
        symbols = (["+"] if expression[0] != "-" else []) + [x for x in expression if x == "-" or x == "+"]
        print(nums)
        print(symbols)
        a, b = 0, 1
        for i in range(len(nums)):
            c, d = nums[i].split("/")
            c = int(c) if symbols[i] == "+" else int("-" + c)
            d = int(d)
            x, y = add(a, b, c, d)
            a, b = x, y
        return str(a) + "/" + str(b)

