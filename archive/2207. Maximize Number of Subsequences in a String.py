class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        text = [ch for ch in text if ch in pattern]
        ca,cb=text.count(pattern[0]),text.count(pattern[1])
        if pattern[0]==pattern[1]:
            return (ca+1)*ca//2


        if ca>cb:
            text.append(pattern[1])
        else:
            text.insert(0,pattern[0])
        ca,cb=text.count(pattern[0]),text.count(pattern[1])
        # print(text,ca,cb)
        ans=0
        for ch in text:
            if ch==pattern[0]:
                ans+=cb
            else:
                cb-=1
        return ans



text="fwymvreuftzgrcrxczjacqovduqaiig"
pattern="yy"
print(Solution().maximumSubsequenceCount(text,pattern))