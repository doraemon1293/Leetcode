class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        A,B=toBeRemoved
        ans=[]
        for interval in enumerate(intervals):
            lo,hi=interval
            if A>=hi or B<=lo:
                ans.append([interval])
            else:
                if A<hi:
                    ans.append([lo,A])
                if B>lo:
                    ans.append([B,hi])
        return ans



