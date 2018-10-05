import random
class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.d = {}
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.end=self.n_cols*self.n_rows-1

    def flip(self):
        """
        :rtype: List[int]
        """
        temp=random.randint(self.start,self.end)
        res=self.d.get(temp,temp)
        seld.d[res]=self.d[self.start,self.start]
        return [res//self.n_cols,res%self.n_cols]

    def reset(self):
        """
        :rtype: void
        """
        self.d.={}
        self.start=0

# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
