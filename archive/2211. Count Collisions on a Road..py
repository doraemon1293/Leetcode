class Solution:
    def countCollisions(self, directions: str) -> int:
        stack=[]
        ans=0
        for d in directions:
            stack.append(d)
            p=len(stack)-1
            while p>=1 and (stack[p-1],stack[p]) in (("S","L"),("R","L"),("R","S")):
                if (stack[p-1],stack[p]) ==("S","L"):
                    stack[p-1]="S"
                    stack[p]="S"
                    ans+=1
                elif (stack[p-1],stack[p]) ==("R","L"):
                    stack[p-1]="S"
                    stack[p]="S"
                    ans+=2
                elif (stack[p-1],stack[p]) == ("R","S"):
                    stack[p-1]="S"
                    stack[p]="S"
                    ans+=1
                p-=1
            # print(stack,ans)
        return ans

direction="SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
Solution().countCollisions(direction)
