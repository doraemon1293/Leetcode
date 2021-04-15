class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        if "0" not in binary:
            return binary
        zero = binary.index('0')

        p1 = binary[:zero]
        p2 = binary[zero:].count("0") * "0"
        p3 = binary[zero:].count("1") * "1"
        ans = p1 + (len(p2) - 1) * "1" + "0" + p3
        return ans
