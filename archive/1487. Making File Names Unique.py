class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        all_names = set()
        d = {}
        for name in names:
            if name not in all_names:
                ans.append(name)
                all_names.add(name)
            else:
                k = d.get(name, 0)
                k += 1
                while "{}({})".format(name, k) in all_names:
                    k += 1
                d[name] = k
                ans.append("{}({})".format(name, k))
                all_names.add("{}({})".format(name, k))
        return ans

