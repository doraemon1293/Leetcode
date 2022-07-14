class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        armor=max(armor,max(damage))
        return sum(damage)-armor+1