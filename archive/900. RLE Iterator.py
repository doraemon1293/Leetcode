class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A=A
        self.ind=0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.ind<len(self.A) and n:
            if self.A[self.ind+1]<n:
                n-=self.A[self.ind+1]
                self.ind+=2
            else:
                self.A[self.ind+1]-=n
                n=0
        if n==0:
            return self.A[self.ind]
        else:
            return -1






# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)