class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s)>k:
            new_s=[]
            for i in range(0,len(s),k):
                temp=s[i:i+k]
                new_s.append(sum([int(ch) for ch in temp]))
            s="".join(new_s)
        return s

