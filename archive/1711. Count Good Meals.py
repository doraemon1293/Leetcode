from typing import List
import collections
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        twos=[1]
        for _ in range(21):
            twos.append(twos[-1]<<1)
        print(twos)
        c=collections.Counter(deliciousness)
        nums=sorted(set(deliciousness))
        ans=0
        MOD = 10 ** 9 + 7

        for num1 in nums:
            for two in twos:
                num2=two-num1
                if num2>=num1 and num2 in c:
                    if num1==num2:
                        ans+=c[num1]*(c[num1]-1)//2
                    else:
                        ans+=c[num1]*c[num2]
        return ans%MOD


print(Solution().countPairs(deliciousness=[149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234]))
