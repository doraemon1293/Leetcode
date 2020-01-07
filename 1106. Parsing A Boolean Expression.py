import functools


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        ops = []
        exps = [[]]

        def op_and(x, y):
            return x and y

        def op_or(x, y):
            return x or y

        for ch in expression:
            if ch in ("!", "&","|"):
                ops.append(ch)
            if ch == "(":
                exps.append([])
            if ch == "f":
                exps[-1].append(False)
            if ch == "t":
                exps[-1].append(True)
            if ch == ")":
                # print(exps)
                # print(ops)
                exp = exps.pop()
                op = ops.pop()
                if op == "!":
                    exps[-1].append(not exp[0])
                if op == "&":
                    val =functools.reduce(op_and,exp)
                    exps[-1].append(val)
                if op == "|":
                    val =functools.reduce(op_or,exp)
                    exps[-1].append(val)
        return exps[0][0]
expression = "|(&(t,f,t),!(t))"
print(Solution().parseBoolExpr(expression))