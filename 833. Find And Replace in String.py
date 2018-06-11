class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        arr=[]
        for i in range(len(indexes)):
            index=indexes[i]
            source=sources[i]
            target=targets[i]
            if S[index:].startswith(source):
                arr.append((index,index+len(source),target))
        arr.sort()
        print(arr)
        p=0
        ans=""
        ind=0
        while p<len(S):
            if ind<len(arr) and p>=arr[ind][0]:
                st,end,target=arr[ind]
                ans+=target
                p=end
                ind+=1
            else:
                ans+=S[p]
                p+=1
        return ans

S="abcd"
indexes=[0, 2]
sources=["a", "cd"]
targets=["eee", "ffff"]

S="abcd"
indexes=[0, 2]
sources=["ab", "ec"]
targets=["eee", "ffff"]

S="vmokgggqzp"
indexes=[3,5,1]
sources=["kg","ggq","mo"]
targets=["s","so","bfr"]
print(Solution().findReplaceString(S,indexes,sources,targets))





