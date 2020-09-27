class Solution:
    def longestAwesome(self, s: str) -> int:
        seen={0:-1}
        cur=0
        ans=0
        valid_status_set=set([0])
        for i in range(10):
            valid_status_set.add(1<<i)

        for i,digit in enumerate(s):
            digit=int(digit)
            cur^=(1<<digit)
            for valid_status in valid_status_set:
                temp=cur^valid_status
                if temp in seen:
                    ans=max(ans,i-seen[temp])
            seen[cur]=min(seen.get(cur,len(s)),i)
        return ans





s = "3242415"
# s="10120"
s=eval(open("../input", "r").readline())
print(Solution().longestAwesome(s))
