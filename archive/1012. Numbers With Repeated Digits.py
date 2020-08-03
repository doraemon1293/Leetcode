import math


class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        def no_repeat_digits_number(length):
            return 9 * math.factorial(9) // math.factorial(9 - (length - 1))

        def no_repeat_digits_number2(digits, length):
            return math.factorial(digits) // math.factorial(digits - length)

        self.ans = 0
        for i in range(1, len(str(N))):
            self.ans += no_repeat_digits_number(i)
        print(self.ans)

        def foo(N, used_digit, first):
            st = 1 if first else 0
            if len(N) == 1:
                print(N,used_digit,first)
                return len([i for i in range(st,int(N)+1) if i not in used_digit])
            res = 0
            for i in range(st, int(N[0])):
                if i not in used_digit:
                    res += no_repeat_digits_number2(10 - len(used_digit) - 1, len(N) - 1)
            if int(N[0]) not in used_digit:
                used_digit.add(int(N[0]))
                res += foo(N[1:], used_digit, False)
            print(res, N, used_digit, first)
            return res

        res = foo(str(N), set(), True)
        print(res)
        return N - (self.ans + res)


N = 3432532
print(Solution().numDupDigitsAtMostN(N))
