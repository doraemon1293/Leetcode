import fractions
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        lines=0
        current_line=fractions(float("inf"))
        stockPrices.sort()
        for i in range(1,len(stockPrices)):
            x1,y1=stockPrices[i-1]
            x2, y2=stockPrices[i]
            new_line=fractions.Fraction(y2-y1,x2-x1)
            if new_line!=current_line:
                lines+=1
                current_line=new_line
        return lines



