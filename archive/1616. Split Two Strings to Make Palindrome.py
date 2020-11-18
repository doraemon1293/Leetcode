class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def foo(a,b):
            i=0
            while i<len(a)//2 and a[i]==b[-(i+1)]:
                i+=1
            s1=a[i:len(a)-i]
            s2=b[i:len(b)-i]
            print(i)
            print(s1)
            print(s2)
            return s1==s1[::-1] or s2==s2[::-1]
        return foo(a,b) or foo(b,a)

a="abdefv"
b="asfsba"
a = "ulacfd"
b = "jizalu"
print(Solution().checkPalindromeFormation(a,b))