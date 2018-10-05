class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag = None
        for i in range(0, len(A) - 1):
            if A[i] < A[i + 1]:
                if flag is None:
                    flag = False
                elif flag:
                    return False
            elif A[i] > A[i + 1]:
                if flag is None:
                    flag = True
                elif flag == False:
                    return False
        return True
