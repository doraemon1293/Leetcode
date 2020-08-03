class Solution:
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import bisect
        mini = [None] * len(A)  # mini[i] is the min value on right of A[i] and bigger than A[i]
        maxi = [None] * len(A)
        numbers_set = set()
        numbers_set.add(A[-1])
        numbers_arr = [(A[-1], len(A) - 1)]
        for i in range(len(A) - 2, -1, -1):
            a = A[i]
            if a in numbers_set:
                ind = bisect.bisect_left(numbers_arr,(a,i))
                maxi[i] = mini[i] = numbers_arr[ind][1]
                numbers_arr[ind] = (a, i)
            else:
                ind = bisect.bisect_left(numbers_arr,(a,i))
                if ind < len(numbers_arr):
                    mini[i] = numbers_arr[ind][1]
                if ind > 0:
                    maxi[i] = numbers_arr[ind-1][1]
                bisect.insort_left(numbers_arr,(a,i))
                numbers_set.add(a)
        # print(numbers_arr)
        # print(mini)
        # print(maxi)
        dp=[[False,False] for _ in range(len(A))]
        dp[-1]=(True,True)
        res=1
        for i in range(len(A)-2,-1,-1):
            for odd in range(2):
                if odd==0:#odd jump
                    if mini[i]!=None:
                        dp[i][odd]=dp[mini[i]][(odd+1)%2]
                    if dp[i][odd]:
                        res+=1
                else:
                    if maxi[i]!=None:
                        dp[i][odd]=dp[maxi[i]][(odd+1)%2]
        return res




A=[2,3,1,1,4]
print(Solution().oddEvenJumps(A))
