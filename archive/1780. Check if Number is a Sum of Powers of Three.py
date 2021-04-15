class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        arr=[]
        while n:
            arr.append(n%3)
            n//=3
        return [x for x in arr if x==2]==[]