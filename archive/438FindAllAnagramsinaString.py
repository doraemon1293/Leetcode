class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        if len(s) < len(p):
            return []
        sub_counter = Counter(s[:len(p)])
        sub_counter.subtract(Counter(p))
        print sub_counter
        print Counter(s[:len(p)])
        print Counter(p)
        if not filter(lambda x:x != 0, sub_counter.values()):
            ans = [0]
            eq = True
        else:
            ans = []
            eq = False
        for i in range(len(p), len(s)):
            sub_counter.setdefault(s[i], 0)
            sub_counter[s[i]] += 1
            sub_counter[s[i - len(p)]] -= 1
            if eq:
                if s[i] == s[i - len(p)]:
                    ans.append(i - len(p) + 1)
                else:
                    eq = False
            elif not filter(lambda x:x != 0, sub_counter.values()):
                eq = True
                ans.append(i - len(p) + 1)
        return ans


s = "baa"
p = "aa"
print Solution().findAnagrams(s, p)

