import bisect
class RecentCounter(object):

    def __init__(self):
        self.q=[]
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        st=t-3000
        ind=bisect.bisect_left(self.q,st)
        self.q=self.q[ind+1:]
        self.q.append(t)
        return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)