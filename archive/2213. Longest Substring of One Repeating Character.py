from typing import List
from sortedcontainers import SortedList
class Solution:
    def longestRepeating(self, s):#: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        arr=[]
        d={}
        last_ch=None
        for i,ch in enumerate(s+"."):
            if ch !=last_ch:
                if last_ch!=None:
                    arr.append((left,i))
                    d[left,i]=last_ch
                last_ch=ch
                left=i
        arr=SortedList(arr)
        print(arr)
        print(d)
        print(arr.bisect_left((1,2)))
        arr.add((3,3))
        print(arr)

s="aaazz"
Solution().longestRepeating(s)