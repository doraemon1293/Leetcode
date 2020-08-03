class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        N=len(customers)
        summ=sum([customers[i] if grumpy[i]==0 else 0 for i in range(N)] or [0])
        arr=[customers[i] if grumpy[i] else 0 for i in range(N)]
        temp=ans=sum(arr[:X])
        for i in range(N-X):
            temp=temp+(arr[i+X]-arr[i])
            ans=max(ans,temp)

        return summ+ans


