class Solution:
    def minimizeResult(self, expression: str) -> str:
        left,right=expression.split("+")
        left=list(left)
        right=list(right)
        mini=float("inf")
        ans=""
        for i in range(len(left)):
            new_left=left[:]
            if i==0:
                new_left.insert(i,"(")
            else:
                new_left.insert(i, "*(")
            for j in range(1,len(right)+1):
                new_right=right[:]
                if j==len(right):
                    new_right.insert(j,")")
                else:
                    new_right.insert(j, ")*")
                exp="".join(new_left)+"+"+"".join(new_right)
                if eval(exp)<mini:
                    mini=eval(exp)
                    ans=exp.replace("*","")
        return ans


