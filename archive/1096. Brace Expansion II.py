import itertools
class Solution:
    def braceExpansionII(self, expression: str) -> list:
        def parse(s):
            s=s+","
            res=[]#all factors
            factors=[]#cureent factors
            cur_s=""
            i=0
            while i<len(s):
                if s[i].isalpha():
                    cur_s+=s[i]
                    i+=1
                elif s[i]=="{":
                    if cur_s:
                        factors.append({cur_s})
                        cur_s=""
                    stack=["{"]
                    start = i+1
                    i+=1
                    while i<len(s) and stack:
                        if s[i]=="{":
                            stack.append("{")
                        if s[i]=="}":
                            stack.pop()
                        i+=1
                    end=i-1
                    factor=parse(s[start:end])
                    factors.append(factor)
                elif s[i]==",":
                    if cur_s:
                        factors.append({cur_s})
                        cur_s=""
                    res.append(factors)
                    factors=[]
                    i+=1
            temp_set=set()
            for factors in res:
                for product in itertools.product(*factors):
                    temp_set.add("".join(product))
            res=sorted(temp_set)
            return res
        return parse(expression)
expression="{a,b}{c{d,e}}"
expression="{{a,z},a{b,c},{ab,z}}"
print(Solution().braceExpansionII(expression))





