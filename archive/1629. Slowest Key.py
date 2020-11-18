class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        dur=[]
        st=0
        for i in range(len(releaseTimes)):
            end=releaseTimes[i]
            dur.append(end-st)
            st=end
        inds=[keysPressed[i] for i in range(len(dur)) if dur[i]==max(dur)]
        return max(inds)


