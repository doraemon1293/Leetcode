import collections
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        dp = {("", 0, k): 0}
        for i in range(len(s)):
            new_dp = collections.defaultdict(lambda :float("inf"))
            for state, length in dp.items():
                last, count, remain_delete = state
                if s[i] == last:
                    # keep i-th
                    if count == 1 or count == 10 ** (len(str(count))) - 1:
                        new_length = length + 1
                    else:
                        new_length = length
                    new_state = (last, count + 1, remain_delete)
                    new_dp[new_state] = min(new_dp[new_state],new_length)
                    # delete i-th
                    if remain_delete>0:
                        new_state = (last, count , remain_delete-1)
                        new_dp[new_state]=min(new_dp[new_state],length)
                else:
                    #keep i-th
                    new_state=(s[i],1,remain_delete)
                    new_length=length+1
                    new_dp[new_state]=min(new_dp[new_state],new_length)
                    #delete i-th
                    if remain_delete>0:
                        new_state=(last,count,remain_delete-1)
                        new_dp[new_state]=min(new_dp[new_state],length)
            dp=new_dp
        return min(dp.values())
s= "aaabcccd"
k = 2
print(Solution().getLengthOfOptimalCompression(s,k))

