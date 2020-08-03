import collections
class Solution:
    def largestValsFromLabels(self, values: list, labels: list, num_wanted: int, use_limit: int) -> int:
        arr=sorted([(value,label) for value,label in zip(values,labels)],reverse=True)
        ans=0
        d=collections.defaultdict(int)
        for value,label in arr:
            if num_wanted==0:
                break
            if d[label]<use_limit:
                ans+=value
                d[label]+=1
                num_wanted-=1
        return ans

