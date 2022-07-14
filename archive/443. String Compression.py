class Solution:
    def compress(self, chars: List[str]) -> int:
        p1 = p2 = 0
        l = 0
        chars.append(" ")
        while p2 < len(chars):
            if l == 0:
                chars[p1] = chars[p2]
                l += 1
                p1 += 1
            else:
                if chars[p1 - 1] == chars[p2]:
                    l += 1
                else:
                    if l > 1:
                        chars[p1:p1 + len(str(l))] = list(str(l))
                        p1 += len(str(l))
                    chars[p1] = chars[p2]
                    p1 += 1
                    l = 1
            p2 += 1
        return p1 - 1



