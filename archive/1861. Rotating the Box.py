class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        for row in box:
            bot=p=len(row)-1
            while bot>=0:
                empty=stone=0
                while p>=0 and row[p]!="*":
                    if row[p]==".":
                        empty+=1
                    else:
                        stone+=1
                    p-=1
                row[p+1:bot+1]=["."]*empty+["#"]*stone
                p-=1
                bot=p
        # for row in box:
        #     print(row)
        ans=[list(row[::-1]) for row in list(zip(*box))]
        return ans