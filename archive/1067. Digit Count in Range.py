class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def count(n, d):
            if n == 0: return 0
            s = str(n)
            res = 0
            for i in range(len(s)):
                left = s[:i]
                right = s[i + 1:]
                a = int(s[i])
                if a > d:
                    l = int(left) + 1 if left else 1
                    if d == 0:
                        l -= 1
                    r = 10 ** len(right)
                    temp = l * r
                elif a == d:
                    l = int(left) if left else 0
                    if d == 0:
                        l -= 1
                    r = 10 ** len(right)
                    temp = l * r
                    temp += int(right) + 1 if right else 1
                else:  # a<d
                    l = int(left) if left else 0
                    r = 10 ** len(right)
                    temp = l * r
                res += temp
            return res

        return count(high, d) - count(low - 1, d)


d = 3
low = 100
high = 250
print(Solution().digitsCount(d, low, high))
