from typing import List
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def get_val(w):
            res = 0
            w = set(w)
            for ch in w:
                res = (res | (1 << (ord(ch) - ord("a"))))
            return res

        set_ = set()
        for w in startWords:
            val = get_val(w)
            # print(bin(val))
            for i in range(26):
                if (val >> i) & 1 == 0:
                    new_val = (val | (1 << i))
                    # print(bin(new_val))
                    set_.add(new_val)

        return len([w for w in targetWords if get_val(w) in set_])


print(Solution().wordCount(["ant","act","tack"],
["tack","act","acti"]
                           ))