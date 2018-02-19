class Solution:

    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        from collections import Counter

        def lowerPriority(op1, op2):
            """True if op1 has lower prior than op2
            """
            if op1 == "(" or (op1 in ("+", "-") and op2 == "*"):
                return True
            else:
                return False

        def convertInfixToPostfix(expression, d):
            ind = 0
            stack = []
            exp = []
            cur = ""
            while ind < len(expression):
                ch = expression[ind]
                if ch == " ":
                    pass
                elif ch.isalnum():
                    cur += ch
                else:
                    if cur != "":
                        if cur.isdigit():
                            exp.append(Counter({():int(cur)}))
                        else:
                            if cur in d:
                                exp.append(Counter({():d[cur]}))
                            else:
                                exp.append(Counter({(cur,):1}))
                        cur = ""
                    if ch == "(":
                        stack.append(ch)
                    elif ch == ")":
                        while stack[-1] != "(":
                            exp.append(stack.pop())
                        stack.pop()
                    else:  # +-*
                        while stack and not lowerPriority(stack[-1], ch):
                            exp.append(stack.pop())
                        stack.append(ch)
                ind += 1
            if cur != "":
                if cur.isdigit():
                    exp.append(Counter({():int(cur)}))
                else:
                    if cur in d:
                        exp.append(Counter({():d[cur]}))
                    else:
                        exp.append(Counter({(cur,):1}))
            while stack:
                exp.append(stack.pop())
            return exp

        def mul(c1, c2):
            c = Counter()
            for k1, v1 in c1.items():
                for k2, v2 in c2.items():
                    k = tuple(sorted(list(k1) + list(k2)))
                    v = v1 * v2
                    c.update(Counter({k:v}))
            for k in list(c.keys()):
                if c[k] == 0:
                    del c[k]
            return c

        def cal(exp):
            stack = []
            for i in range(len(exp)):
                ch = exp[i]
                if type(ch) == Counter:
                    stack.append(ch)
                else:
                    b, a = stack.pop(), stack.pop()
                    if ch == "+":
                        a.update(b)
                    if ch == "-":
                        a.subtract(b)
                    if ch == "*":
                        a = mul(a, b)
                    for k in list(a.keys()):
                        if a[k] == 0:
                            del a[k]
                    stack.append(a)
            a = stack[-1]
            for k in list(a.keys()):
                if a[k] == 0:
                    del a[k]
            return stack[-1]

        d = {}
        for k, v in zip(evalvars, evalints):
            d[k] = v
        exp = convertInfixToPostfix(expression, d)
        exp = cal(exp)
        ans = []
        const = None
        keys = sorted(list(exp.keys()), key = lambda x:(-len(x), x))
        for k in keys:
            ans.append("*".join([str(exp[k])] + list(k)))
        if const:
            ans.append(str(const))
        return ans


expression = "e - 8 + temperature - pressure"
evalvars = ["e", "temperature"]
evalints = [1, 12]

expression = "0"
evalvars = []
evalints = []

# expression = "a+b+b"
# evalvars = ["a"]
# evalints = [0]

# expression = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))+10"
# evalvars = []
# evalvars = []
print(Solution().basicCalculatorIV(expression, evalvars, evalints))
