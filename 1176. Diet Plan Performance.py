class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        ans=0
        temp=sum(calories[:k])
        if temp < lower:
            ans -= 1
        if temp > upper:
            ans += 1
        for i in range(k,len(calories)):
            temp=temp+calories[i]-calories[i-k]
            if temp<lower:
                ans-=1
            if temp>upper:
                ans+=1
        return ans