class Solution(object):
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        ones = A.count("1")
        if ones % 3:
            return [-1, -1]
        else:
            separators = []
            st = 0
            for _ in range(3):
                while A[st] != "1":
                    st += 1
                end = st
                temp = ones // 3
                while temp:
                    if A[end] == "1":
                        temp -= 1
                    end += 1
                separators += [st, end]
                st = end + 1
            s1, e1, s2, e2, s3, e3 = separators
            if A[s1:e1] == A[s2:e2] == A[s3:e3]:
                tail_zeros = len(A) - e3
                if s2-e1<tail_zeros or s3-e2<tail_zeros:
                    return [-1,-1]
                else:
                    return [e1+tail_zeros-1,e2+tail_zeros-1]
            else:
                return [-1, -1]
