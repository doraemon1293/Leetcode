from typing import List
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chef=0
        wait=0
        for a,b in customers:
            if chef<a:
                chef=a
            chef+=b
            wait+=chef-a
        return wait/len(customers)


