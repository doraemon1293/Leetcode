class Solution:
    def confusingNumber(self, N: int) -> bool:
        d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        N1 = []
        for ch in str(N):
            ch1 = d.get(ch)
            if ch1 == None:
                return False
            N1.append(ch1)
        return str(N) != "".join(N1[::-1])