from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(arr) for arr in languages]
        temp = []
        for a, b in friendships:
            if len(languages[a - 1] & languages[b - 1]) == 0:
                temp.append((a-1, b-1))
        friendships = temp
        # print(friendships)

        ans = float("inf")
        for lang in range(1, n + 1):
            temp = 0
            known = set()
            for a,b in friendships:
                if lang not in languages[a] and a not in known:
                    known.add(a)
                    temp+=1
                if lang not in languages[b] and b not in known:
                    known.add(b)
                    temp += 1

            ans = min(ans, temp)
        return ans


print(Solution().minimumTeachings(n=3, languages=[[2], [1, 3], [1, 2], [3]],
                                  friendships=[[1, 4], [1, 2], [3, 4], [2, 3]]))
