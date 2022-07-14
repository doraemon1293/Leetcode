class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        arr=[0]*(n+1)
        for light in lights:
            p,r=light
            arr[max(0,p-r)]+=1
            arr[min(n,p+r+1)]-=1
        bright=0
        ans=0
        for i in range(n):
            bright+=arr[i]
            ans+=(bright>=requirement[i])
        return ans

