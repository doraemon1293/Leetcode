from typing import List


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        def get_min(arr, target, add):
            res = 0
            lo, hi = 0, target
            while lo <= hi:
                mid = (lo + hi) // 2
                new_arr = [max(0, mid - x) for x in arr]
                summ = sum(new_arr)
                if summ <= add:
                    lo = mid + 1
                    res = max(res, mid)
                else:
                    hi = mid - 1
            return res





        flowers.sort(reverse=True)
        i = 0
        while i < len(flowers) and flowers[i] >= target:
            i += 1
        full_number = i

        ans = full_number * full
        if full_number==len(flowers):#edge case
            return ans

        # if newFlowers >= target * len(flowers) - sum(flowers):#edge case
        #     return max(full*len(flowers), full*(len(flowers)-1) + partial*(target-1))




        flowers = flowers[i:]
        summ = sum(flowers)
        length = len(flowers)
        print(full_number,flowers)






        for i, flower in enumerate(flowers):


            min_value = min(target - 1, (summ + newFlowers) // length)
            print(summ,newFlowers,length,min_value,full_number)

            ans = max(ans, full_number * full + min_value * partial)

            if newFlowers >= target - flower:
                full_number += 1
                newFlowers -= target - flower
            else:
                break
            summ -= flower
            length -= 1
        ans = max(ans, full_number * full)
        return ans


flowers = [1, 3, 1, 1]
newFlowers = 7
target = 6
full = 12
partial = 1

flowers = [20, 1, 15, 17, 10, 2, 4, 16, 15, 11]
newFlowers = 2
target = 20
full = 10
partial = 2

print(Solution().maximumBeauty(flowers, newFlowers, target, full, partial))
