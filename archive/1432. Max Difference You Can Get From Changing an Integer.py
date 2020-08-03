class Solution:
    def maxDiff(self, num: int) -> int:
        s1 = str(num)
        s2 = str(num)
        for i in range(len(s1)):
            if s1[i] != "9":
                s1 = s1.replace(s1[i], "9")
                break

        if s2[0] != "1":
            s2 = s2.replace(s2[0], "1")
        else:
            for i in range(1, len(s2)):
                if s2[i] not in ("0", "1"):
                    s2 = s2.replace(s2[i], "0")
                    break
        return int(s1) - int(s2)
