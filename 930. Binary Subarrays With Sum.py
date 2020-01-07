class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        if S==0:
            ans=0
            zeros=0
            A.append(1)
            for a in A:
                if a==0:
                    zeros+=1
                else:
                    ans+=zeros*(1+zeros)//2
                    zeros=0
            return ans
        else:

            ans = 0
            cur_sum = 0
            p1 = p2 = 0
            while p2 < len(A):
                while p2 < len(A) and cur_sum < S:
                    cur_sum += A[p2]
                    p2 += 1
                zeros = 1
                while p2 < len(A) and A[p2] == 0:
                    p2 += 1
                    zeros += 1
                print(p1,p2,zeros)
                while p1 < p2 and cur_sum == S:
                    ans+=zeros
                    cur_sum-=A[p1]
                    p1+=1
            return ans


A = [0, 0, 0, 0, 0]
S = 0
A = [1, 0, 1, 0, 1]
S = 2
print(Solution().numSubarraysWithSum(A, S))
