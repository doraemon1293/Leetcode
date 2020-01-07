class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list:
        times = int((-1 + (1 + 8 * candies) ** 0.5) // 2)
        turns = times // num_people
        remain = times % num_people
        print(times, turns, remain)
        ans = [0] * num_people
        for i in range(num_people):
            ans[i] = ((i + 1) + (i + 1 + (turns - 1) * num_people)) * turns // 2
            if i + 1 <= remain:
                ans[i] += (i + 1) + turns * num_people
            if i + 1 == remain + 1:
                ans[i] += candies - (1 + times) * times // 2
        return ans


candies = 10
num_people = 3
print(Solution().distributeCandies(candies, num_people))
