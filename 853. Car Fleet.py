class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        arr=sorted([(position[i],i) for i in range(len(position))],reverse=True)
        fleet=0
        last_t=-float("inf")

        for pos,ind in arr:
            t=(target-pos)/speed[ind]
            if t<=last_t:
                continue
            else:
                fleet+=1
                last_t=t
        return fleet