class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        stack=[]
        s=s+"_"
        for ch in s:
            if ch in ("a","b"):
                stack.append(ch)
                if x>=y and len(stack)>=2 and stack[-2]+stack[-1]=="ab":
                    ans+=x
                    stack.pop()
                    stack.pop()
                if y>x and len(stack)>=2 and stack[-2]+stack[-1]=="ba":
                    ans+=y
                    stack.pop()
                    stack.pop()
            else:
                b_=a_=0
                for i in range(len(stack)):
                    if stack[i]=="a":
                        a_+=1
                    else:
                        b_+=1
                if x>=y:
                    ans+=y*min(a_,b_)
                else:
                    ans+=x*min(a_,b_)
                stack=[]

        return ans
