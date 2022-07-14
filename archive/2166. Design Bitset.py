class Bitset:

    def __init__(self, size: int):
        self.bit=["0"]*size
        self.ones=0
        self.flips=False

    def value_at_idx(self,idx):
        if self.flips:
            return "0" if self.bit[idx]=="1" else "1"
        else:
            return self.bit[idx]

    def set_value_at_idx(self,idx,value):
        if self.flips:
            self.bit[idx]="0" if value=="1" else "1"
        else:
            self.bit[idx]=value

    def fix(self, idx: int) -> None:
        if self.value_at_idx(idx)=="0":
            self.ones+=1
            self.set_value_at_idx(idx,"1")


    def unfix(self, idx: int) -> None:
        if self.value_at_idx(idx)=="1":
            self.ones-=1
            self.set_value_at_idx(idx,"0")

    def flip(self) -> None:
        self.flips=not self.flips
        self.ones=len(self.bit)-self.ones

    def all(self) -> bool:
        return self.ones==len(self.bit)

    def one(self) -> bool:
        return self.ones>0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        if self.flips:
            return "".join(["0" if ch=="1" else "1" for ch in self.bit])
        else:
            return "".join(self.bit)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()