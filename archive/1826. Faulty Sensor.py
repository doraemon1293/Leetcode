class Solution(object):
    def badSensor(self, sensor1, sensor2):
        """
        :type sensor1: List[int]
        :type sensor2: List[int]
        :rtype: int
        """
        ind = 0
        while ind <= len(sensor1) and sensor1[ind] == sensor2[ind]:
            ind += 1
        if ind == len(sensor1):
            return -1
        if ind==len(sensor1)-1:
            return -1
        if sensor1[ind+1:]==sensor2[ind:-1]:
            return 2

        if sensor2[ind + 1:] == sensor1[ind:-1]:
            return 1
        return -1