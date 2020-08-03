from collections import defaultdict


class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        def get_new_to_sort(to_sort, col):
            new_to_sort = []
            for arr in to_sort:
                temp = [col[x] for x in arr]
                sorted_temp = sorted(temp)
                if temp == sorted_temp:
                    d = defaultdict(list)
                    for i, ch in zip(arr,temp):
                        d[ch].append(i)
                    new_to_sort.extend([x for x in d.values() if len(x)>1])
                else:
                    return False
            return new_to_sort

        to_sort = [list(range(len(A)))]
        ans = 0
        for col in zip(*A):
            new_to_sort = get_new_to_sort(to_sort, col)
            if new_to_sort == False:
                ans += 1
            else:
                to_sort = new_to_sort
        return ans


A = ["zyx", "wvu", "tsr"]
#A = ["xc", "yb", "za"]
#A=["hdbbaomiyk","amcdtrnhjn","fheqnqdkjq","mfeluiclbm","jkexmcstwn","egfmxwjxdj","ayhowbifcx","swhykufgfk","vxhdwxuhwj","johfdcfojv","rnircklfcm","lzkwfqomcz","fvkkhzomgb","aukuoedptv","eimzwmlgxj","ptmnmgppso","oknfgdtweb","mtnukewwir","nlowbhwjdm","tcovbbvuuw","ilqyvtgnfv","nrqgupdyyg","wnrdwmsnzt","rosqrtdeus","bysheeghqg","ciswvgqqlf","uwteztkmqf","tbumqubzdb","dqxbfiwuvm","atxbvdiywo"]
print(Solution().minDeletionSize(A))
