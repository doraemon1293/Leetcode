# coding=utf-8
'''
Created on 2017å¹?11æœ?12æ—?

@author: Administrator
'''


class Solution(object):

    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        from collections import defaultdict

        def getName(i):
            name = [formula[i]]
            i += 1
            while i < len(formula) and "a" <= formula[i] <= "z":
                name.append(formula[i])
                i += 1
            return "".join(name), i

        def getNum(i):
            num = [formula[i]]
            i += 1
            while i < len(formula) and "0" <= formula[i] <= "9":
                num.append(formula[i])
                i += 1
            return int("".join(num)), i

        def para(i):
            subCounter = defaultdict(int)
            name = None
            while i < len(formula) and formula[i] != ")":
                if formula[i] == "(":
                    if name:
                        subCounter[name] += 1
                        name = None
                    i += 1
                    subSubCounter, i = para(i)
                    for key in subSubCounter:
                        subCounter[key] += subSubCounter[key]
                elif "A" <= formula[i] <= "Z":
                    if name:
                        subCounter[name] += 1
                    name, i = getName(i)
                elif "0" <= formula[i] <= "9":
                    num, i = getNum(i)
                    subCounter[name] += num
                    name = None
            if name:
                subCounter[name] += 1
            i += 1
            if i < len(formula) and "0" <= formula[i] <= "9":
                num, i = getNum(i)
                for name in subCounter:
                    subCounter[name] *= num
            return subCounter, i

        i = 0
        counter = defaultdict(int)
        name = None
        while i < len(formula):
            if "A" <= formula[i] <= "Z":
                if name:
                    counter[name] += 1
                name, i = getName(i)
            elif "0" <= formula[i] <= "9":
                num, i = getNum(i)
                counter[name] += num
                name = None
            elif formula[i] == "(":
                if name:
                    counter[name] += 1
                    name = None
                i += 1
                subCounter, i = para(i)
                for key in subCounter:
                    counter[key] += subCounter[key]
        if name:
            counter[name] += 1
        keys = sorted(counter.keys())
        ans = []
        for key in keys:
            ans.append(key)
            if counter[key] > 1: ans.append(str(counter[key]))
        return "".join(ans)


formula = "K4(ON(SO3)2)2"
print Solution().countOfAtoms(formula)

