class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_per(s):
            for i in range(len(s) - 2, -1, -1):
                if s[i] < s[i + 1]:
                    break
            for j in range(len(s) - 1, i, -1):
                if s[j] > s[i]:
                    break

            s[i], s[j] = s[j], s[i]
            s[i+1:]=s[i+1:][::-1]
            return s
        num0=list([int(x) for x in num])
        num1=num0[:]
        for i in range(k):
            next_per(num1)
        ans=0
        for i in range(len(num)):
            if num0[i]!=num1[i]:
                j=i
                while num1[j]!=num0[i]:
                    j+=1
                ans+=j-i
                num1[i:j+1]=[num1[j]]+num1[i:j]
        return ans