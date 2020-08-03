class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        arr=[abs(ord(a)-ord(b)) for a,b in zip(s,t)]
        length=summ=0
        for end in range(len(arr)):
            if summ+arr[end]<=maxCost:
                summ+=arr[end]
                length+=1
            else:
                summ=summ-arr[end-length]+arr[end]
        return length
