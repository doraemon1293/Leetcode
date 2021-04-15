class NumArray:

    def __init__(self, nums: List[int]):
        self.max_len=len(nums)
        self.nums=[0]*(self.max_len+1)
        self.tree=[0]*(self.max_len+1)
        for i,num in enumerate(nums):
            self.update(i,num)

    def update(self, ind: int, val: int) -> None:
        i=ind+1
        delta=val-self.nums[i]
        while i<=self.max_len:
            self.tree[i]+=delta
            i+=i&(-i)
        self.nums[ind+1]=val


    def sumPrefix(self,n):
        ind=n
        res=0
        while ind>0:
            res+=self.tree[ind]
            ind-=ind&(-ind)
        return res


    def sumRange(self, left: int, right: int) -> int:
        return self.sumPrefix(right+1)-self.sumPrefix(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)