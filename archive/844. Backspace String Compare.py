class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s=[]
        for ch in S:
            if ch=="#":
                if s:
                    s.pop()
            else:
                s.append(ch)
        t=[]
        for ch in T:
            if ch=="#":
                if t:
                    t.pop()
            else:
                t.append(ch)
        return s==t


S="ab#c"
T="ad#c"
print(Solution().backspaceCompare(S,T))