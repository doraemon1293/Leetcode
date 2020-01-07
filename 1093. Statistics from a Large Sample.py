class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        # min
        for i in range(len(count)):
            if count[i]:
                mini = i
                break

        # max
        for i in range(len(count) - 1, -1, -1):
            if count[i]:
                maxi = i
                break

        # mod
        temp = [0, 0]
        for i in range(len(count)):
            if count[i] > temp[0]:
                temp = [count[i], i]
        mod = temp[1]

        # median
        n = sum(count)
        target = (n + 1) // 2
        i = 0
        while count[i] < target:
            target -= count[i]
            i += 1
        if n % 2:
            median = i
        else:
            if target == count[i]:
                temp = i
                i += 1
                while count[i] == 0:
                    i += 1
                median=(temp+i)/2
            else:
                median=i
        #mean
        temp=0
        for i in range(len(count)):
            temp+=i*count[i]
        mean=temp/n


        return [float(x) for x in [mini,maxi,mean,median,mod]]
