class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        arr=text.split(" ")
        ans=[]
        for i in range(len(arr)-2):
            if arr[i]==first and arr[i+1]==second:
                ans.append(arr[i+2])
        return ans
