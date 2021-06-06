class Solution(object):
    def memLeak(self, memory1, memory2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """
        seconds=0
        while memory1>=seconds or memory2>=seconds:
            if memory1>=seconds and memory2>=seconds:
                if memory2>memory1:
                    memory2-=seconds
                else:
                    memory1-=seconds
            elif memory1>=seconds:
                memory1-=seconds
            elif memory2>=seconds:
                memory2-=seconds
            seconds+=1
        return [seconds,memory1,memory2]