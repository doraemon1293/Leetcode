class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = {}
        for people, start, end in trips:
            d.setdefault(start, 0)
            d[start] += people
            d.setdefault(end, 0)
            d[end] -= people
        people=0
        for k in sorted(d.keys()):
            people+=d[k]
            if people>capacity:
                return False
        return True

