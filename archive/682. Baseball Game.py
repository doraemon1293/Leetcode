class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans=0
        stack=[]
        for op in ops:
            if op[0]=="-" and op[1:].isdigit() or op.isdigit():
                ans+=int(op)
                stack.append(int(op))
            elif op=="+":
                ans+=stack[-1]+stack[-2]
                stack.append((stack[-1]+stack[-2]))
            elif op=="D":
                ans+=stack[-1]*2
                stack.append(stack[-2]*2)
            elif op=="C":
                ans-=stack[-1]
                stack.pop()
        return ans