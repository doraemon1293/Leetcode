class Solution:
    def clumsy(self, N: int) -> int:
        def op(x, y, ch):
            if ch == "+":
                return x + y
            if ch == "-":
                return x - y
            if ch == "*":
                return x * y
            if ch == "/":
                return x // y

        def cal(arr):
            stack_number = []
            stack_operator = []
            for x in arr:
                if type(x) == int:
                    stack_number.append(x)
                else:
                    while stack_operator and not (stack_operator[-1] in ("+", "-") and x in ("/", "*")):
                        y = stack_number.pop()
                        a = stack_number.pop()
                        ch = stack_operator.pop()
                        stack_number.append(op(a, y, ch))
                    stack_operator.append(x)
            while stack_operator:
                y = stack_number.pop()
                x = stack_number.pop()
                ch = stack_operator.pop()
                stack_number.append(op(x, y, ch))

            return stack_number[0]

        n = 0
        arr = []
        for i in range(N, 0, -1):
            arr.append(i)
            if i != 1:
                if n % 4 == 0:
                    arr.append("*")
                if n % 4 == 1:
                    arr.append("/")
                if n % 4 == 2:
                    arr.append("+")
                if n % 4 == 3:
                    arr.append("-")
            n += 1
        print(arr)
        ans = cal(arr)
        return ans


print(Solution().clumsy(10))
