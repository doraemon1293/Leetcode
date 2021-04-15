from typing import List

import re


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = dict((k, v) for k, v in knowledge)
        def foo(m):
            # print(m.group(1))
            return knowledge.get(m.group(1), "?")
        # print(re.findall(r"\(w+\)",s))
        s = re.sub(r"\((\w+)\)", foo, s)
        return s


print(Solution().evaluate(s="(name)is(age)yearsold", knowledge=[["name", "bob"], ["age", "two"]]))
