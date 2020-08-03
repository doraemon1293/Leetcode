class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N==1:
            return list(range(0,10))
        arr=set(range(1,10))
        for _ in range(N-1):
            new_arr=set()
            for num in arr:
                a=num%10
                for aa in (a+K,a-K):
                    if 0<=aa<=9:
                        new_arr.add(num*10+aa)
            arr=new_arr
        return list(arr)
print(Solution().numsSameConsecDiff(2,0))



