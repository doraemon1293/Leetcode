import datetime
from typing import List
import collections


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = collections.defaultdict(list)
        ans = []
        for name, t in zip(keyName, keyTime):
            t = datetime.datetime.strptime(t, "%H:%M")
            d[name].append(t)
        for k in d:
            d[k].sort()
            for i in range(2, len(d[k])):
                if d[k][i] - d[k][i - 2] <= datetime.timedelta(hours=1):
                    ans.append(k)
                    break
        ans.sort()
        return ans