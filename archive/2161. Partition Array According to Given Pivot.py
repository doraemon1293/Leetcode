class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a=[]
        b=[]
        c=[]
        for num in nums:
            if num<pivot:
                a.append(num)
            elif num==pivot:
                b.append(num)
            else:
                c.append(num)
        return a+b+c