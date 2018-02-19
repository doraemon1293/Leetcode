class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = []
        for s in strs:
            res.append(str(len(s)) + "\"" + s + "\"")
        return "".join(res)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        ind = 0
        while ind < len(s):
            length = 0
            while s[ind].isdigit():
                length = length * 10 + int(s[ind])
                ind += 1
            x = s[ind + 1:ind + 1 + length]
            res.append(x)
            ind = ind + 1 + length + 1
        return res


strs = ["abc", "edf", "erf"]
# Your Codec object be instantiated and called as such:
codec = Codec()
print codec.encode(strs)
print codec.decode(codec.encode(strs))
