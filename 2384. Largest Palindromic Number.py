import collections


class Solution:
    def largestPalindromic(self, num: str) -> str:
        ans = []
        c = collections.Counter(num)
        mid = None
        for i in range(9, -1, -1):
            ch = chr(ord('0') + i)
            while ch in c and c[ch] > 1:
                ans.append(ch)
                c[ch] -= 2
            if c[ch]==1 and mid==None:
                mid=ch
        ans = "".join(ans)
        ans = ans.lstrip('0')
        if mid!=None:
            ans = ans + mid + ans[::-1]
        else:
            ans = ans + ans[::-1]
        if ans=="":
            if '0' in num:
                ans='0'
        return ans