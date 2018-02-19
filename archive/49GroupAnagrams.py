class Solution(object):

    def groupAnagrams(self, strs):
        d = {}
        for s in strs:
            key = tuple(sorted(s))
            d.setdefault(key, [])
            d[key].append(s)
        return d.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print Solution().anagrams(strs)
