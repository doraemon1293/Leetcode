import collections
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        c_s=collections.Counter(s)
        c_t=collections.Counter(t)
        return sum([abs(c_s.get(k,0)-c_t.get(k,0)) for k in set(c_s.keys()+c_t.keys())])