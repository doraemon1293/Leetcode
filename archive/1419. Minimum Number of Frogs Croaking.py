class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        s = "croak"
        ans = 0
        frogs = [0] * 4

        for ch in croakOfFrogs:
            print(frogs)
            ind = s.index(ch)
            if ind == 0:
                frogs[0] += 1
                ans = max(frogs[0], ans)
            else:
                if frogs[ind - 1] == 0:
                    return -1
                else:
                    frogs[ind - 1] -= 1
                    if ind != 4:
                        frogs[ind] += 1
            ans = max(sum(frogs), ans)
        if sum(frogs)==0:
            return ans
        else:
            return -1


croakOfFrogs = "croakcroa"
print(Solution().minNumberOfFrogs(croakOfFrogs))
