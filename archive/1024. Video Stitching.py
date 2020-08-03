class Solution:
    def videoStitching(self, clips, T: int) -> int:
        clips.sort()
        print(clips)
        left = -1
        right = 0
        res = 0
        for st, end in clips:
            if st > right:
                return -1
            elif left < st <= right:
                res += 1
                left = right
            right = max(right, end)
            if right >= T:
                return res
        return -1


clips = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5],
         [5, 7], [6, 9]]
T = 9
print(Solution().videoStitching(clips, T))
