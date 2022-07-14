class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d={}
        for i,j in enumerate(mapping):
            d[str(i)]=str(j)
        def foo(num,i):
            res=int("".join([d[ch] for ch in str(num)]))
            return (res,i,num)

        nums=sorted([foo(num,i) for i,num in enumerate(nums)])
        return [x[2] for x in nums]


