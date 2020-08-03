class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list:
        max_depth=depth=0
        depths=[]
        for i,ch in enumerate(seq):
            if ch=="(":
                depth+=1
                depths.append(depth)
                max_depth=max(max_depth,depth)
            if ch==")":
                depths.append(depth)
                depth-=1
        half=max_depth//2
        print(half)
        print(depths)
        return [0 if depth>half else 1 for depth in depths]

seq="(()())"
print(Solution().maxDepthAfterSplit(seq))


