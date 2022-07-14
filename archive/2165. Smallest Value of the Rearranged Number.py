from typing import List
import collections


class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        flag = s[0] != "-"
        if flag:
            c = collections.Counter(s)
            c["0"] = 0 if "0" not in c else c["0"]
            k = sorted(c.keys())
            if len(k) > 1:
                res = k[1]
                c[k[1]] -= 1
                for key in k:
                    res += key * c[key]
                return int(res)
            else:
                return 0


        else:
            c = collections.Counter(s[1:])
            k = sorted(c.keys(), reverse=True)
            res = "-"
            for key in k:
                res += key * c[key]
            return int(res)
print(Solution().smallestNumber(0))