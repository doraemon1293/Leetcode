import functools
class Solution:
    def minimumBoxes(self, n: int) -> int:
        @functools.lru_cache(None)
        def f(layer):
            if layer==0:
                return 0
            else:
                return f(layer-1)+(1+layer)*layer//2
        layer=0
        while f(layer+1)<=n:
            layer+=1
            # print(layer, f(layer))
        n-=f(layer)
        summ=i=0
        while summ<n:
            i+=1
            summ+=i
        # print(layer,i)
        return (1+layer)*layer//2+i


        # return n-f(layer-1)
print(Solution().minimumBoxes(1000))