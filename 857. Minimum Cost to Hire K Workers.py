class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        import heapq
        N=len(wage)
        arr=sorted([(wage[i]/quality[i],quality[i]) for i in range(N)])
        heap=[-arr[i][1] for i in range(K)]
        heapq.heapify(heap)
        cur_q=-sum(heap)
        ratio=arr[K-1][0]
        ans=cur_q*ratio
        for ratio,q in arr[K:]:
            heapq.heappush(heap,-q)
            temp_q=-heapq.heappop(heap)
            cur_q=cur_q+q-temp_q
            ans=min(ans,cur_q*ratio)
        return ans

wage=[70,50,30]
quality=[10,20,5]
K=2

print(Solution().mincostToHireWorkers(quality,wage,K))






