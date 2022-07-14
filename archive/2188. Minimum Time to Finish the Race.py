class Solution(object):
    def minimumFinishTime(self, tires, changeTime, numLaps):
        """
        :type tires: List[List[int]]
        :type changeTime: int
        :type numLaps: int
        :rtype: int
        """
        mini = min(tires)[0]
        dp = [0] * (numLaps + 1)
        dp[1] = mini
        f=[None]*20
        f[0]=[0]*len(tires)
        f[1]=[x[0] for x in tires]
        for i in range(2,20):
            f[i]=[f[i-1][j]+tires[j][0]*(tires[j][1]**(i-1)) for j in range(len(tires))]
        f=[min(f[i]) for i in range(len(f))]
        # print(f)
        temp = [x[0] for x in tires]
        for _ in range(2, min(numLaps + 1, 20)):
            temp = [temp[i] * tires[i][1] for i in range(len(tires))]
            f.append(min(temp))

        for i in range(2, numLaps + 1):
            if i < 20:
                temp = f[i]
            else:
                temp = dp[i - 19] + changeTime + f[19]
            for j in range(i-18, i):
                if j>=1:
                    temp = min(temp, dp[j] + changeTime + f[i - j])
            dp[i] = temp
            # print(dp)
        return dp[numLaps]
tires=[[2,3],[3,4]]
ct=5
numLaps=4
print(Solution().minimumFinishTime(tires,ct,numLaps))