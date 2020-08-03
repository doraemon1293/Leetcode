class Solution:
    def minSwaps(self, data: list) -> int:
        ones=sum(data)
        temp=sum(data[:ones])
        ans=ones-temp
        for i in range(1,len(data)-ones):
            temp=temp-data[i-1]+data[i+ones-1]
            print(temp)
            ans=min(ans,ones-temp)
        return ans
data=[1,0,1,0,1]