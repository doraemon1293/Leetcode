class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        arr=sorted([(g,p) for p,g in zip(plantTime,growTime)],reverse=True)
        cur_days=0
        total_days=0
        for g,p in arr:
            cur_days+=p
            total_days=max(total_days,cur_days+g)
        return total_days