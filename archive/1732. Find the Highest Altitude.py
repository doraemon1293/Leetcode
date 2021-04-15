class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        temp=0
        ans=0

        for x in gain:
            temp+=x
            ans=max(ans,temp

                    )
        return ans