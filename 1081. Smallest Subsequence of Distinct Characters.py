class Solution:
    def smallestSubsequence(self, text: str) -> str:
        chs = set(text)
        ans = ""
        while chs:
            cur_set = set()
            cur_ch = None
            for i in range(len(text) - 1, -1, -1):
                ch = text[i]
                if ch in chs:
                    cur_set.add(ch)
                    if len(cur_set) == len(chs):
                        if cur_ch == None or ch <= cur_ch:
                            cur_ch = ch
                            ind = i
            ans += cur_ch
            chs.remove(cur_ch)
            text = text[ind + 1:]

        return ans


text = "cbaacabcaaccaacababa"
print(Solution().smallestSubsequence(text))
