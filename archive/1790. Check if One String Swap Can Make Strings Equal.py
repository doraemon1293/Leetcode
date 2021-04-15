class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1)==len(s2):
            arr=[i for i in range(len(s1)) if s1[i]!=s2[i]]
            if (len(arr)==2 and s1[arr[0]]==s2[arr[1]] and  s1[arr[1]]==s2[arr[0]]) or arr==[]:
                return True
        return False