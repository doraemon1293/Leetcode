class Solution:
    def removeSubfolders(self, folder: list) -> list:
        root={}
        for s in folder:
            dirs=s.split("/")
            d=root
            for dir in dirs:
                d.setdefault(dir,{})
                d=d[dir]
            d[0]=True
        ans=[]
        def output(pre,d):
            if len(d)==0:
                ans.append("/".join(pre))
            elif 0 in d:
                ans.append("/".join(pre))
            else:
                for k in d:
                    output(pre+[k],d[k])
        output([],root)
        return ans




folder=["/a","/a/b","/c/d","/c/d/e","/c/f"]
print(Solution().removeSubfolders(folder))