import collections


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        diff = None
        counter = collections.Counter(text)
        st = 0
        cur_ch = text[0]
        ans = 1
        i = 0
        while i < len(text):
            if text[i] == cur_ch:
                i += 1
            else:
                if diff == None:
                    diff = i
                    i+=1
                else:
                    ans = max(ans, min(counter[cur_ch], i - st))
                    st = diff
                    cur_ch = text[st]
                    diff = None
                    i = st + 1
        ans = max(ans, min(counter[cur_ch], i - st))
        return ans
