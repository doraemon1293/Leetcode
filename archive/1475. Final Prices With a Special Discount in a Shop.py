class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[None]*len(prices)
        stack=[]
        for i,price in enumerate(prices):
            while stack and stack[-1][0]>=price:
                bigger_price,ind=stack.pop()
                ans[ind]=bigger_price-price
            stack.append((price,i))
        for price,ind in stack:
            ans[ind]=price
        return ans