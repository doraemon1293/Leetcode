# coding=utf-8
class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        from collections import defaultdict
        import bisect
        ch_inds=defaultdict(list)
        for i,ch in enumerate(S):
            ch_inds[ch].append(i)
        ans=0
        for word in words:
            cur=0
            flag=True
            for ch in word:
                ind=bisect.bisect_left(ch_inds[ch],cur)
                if ind==len(ch_inds[ch]):
                    flag=False
                    break
                cur=ch_inds[ch][ind]+1
            if flag:
                print(word)
                ans+=1
        return ans

S="abcde"
words=["a","bb","acd","ace","bd"]
print(Solution().numMatchingSubseq(S,words))




