from typing import List
import collections
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king=kingName
        self.children=collections.defaultdict(list)
        self.dead=set()
    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)


    def getInheritanceOrder(self) -> List[str]:
        self.cur_order=[]
        self.successor(self.king)
        return self.cur_order

    def successor(self,x):
        if x not in self.dead:
            self.cur_order.append(x)
        for child in self.children[x]:
            self.successor(child)






# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()