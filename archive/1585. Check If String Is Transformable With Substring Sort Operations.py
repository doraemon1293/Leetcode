import collections

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        s=list([int(ch)for ch in s])
        t=list([int(ch)for ch in t])
        counter_s=collections.Counter(s)
        counter_t=collections.Counter(t)
        if counter_s!=counter_t:
            return False

        q_s=collections.defaultdict(collections.deque)
        for i,x in enumerate(s):
            q_s[x].append(i)
        # print(q_s)
        for x in t:
            indx=q_s[x].popleft()
            for i in range(x):
                if q_s[i] and q_s[i][0]<indx:
                    return False

        return True