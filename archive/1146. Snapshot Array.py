import collections
import copy
class SnapshotArray:

    def __init__(self, length: int):
        self.arr=collections.defaultdict(int)
        self.snap_shots=[]

    def set(self, index: int, val: int) -> None:
        self.arr[index]=val


    def snap(self) -> int:
        self.snap_shots.append(copy.copy(self.arr))
        return len(self.snap_shots)-1

    def get(self, index: int, snap_id: int) -> int:
        return self.snap_shots[snap_id][index]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)