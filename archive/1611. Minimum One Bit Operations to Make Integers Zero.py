class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        grey_code=[int(x) for x in bin(n)[2:]]
        bin_code=[0]*len(grey_code)
        for i in range(len(grey_code)):
            bin_code[i]=abs((grey_code[i]-(bin_code[i-1] if i>0 else 0)))

        return int("".join([str(x) for x in bin_code]),2)