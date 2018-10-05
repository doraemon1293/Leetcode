class StockSpanner:

    def __init__(self):

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        stack=[]
        res=1
        while stack and stack[0][0]<=price:
            p,span=stack.pop()
            res+=span
        stack.append((price,res))
        return res
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)