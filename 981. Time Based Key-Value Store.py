from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamps=defaultdict(list)
        self.d={}
    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        self.timestamps[key].append(timestamp)
        self.d[key,timestamp]=value


    def get(self, key: 'str', timestamp: 'int') -> 'str':
        ind=bisect.bisect_right(self.timestamps[key],timestamp)
        if ind==0:
            return ""
        else:
            target_timestamp=self.timestamps[key][ind]
            return self.d[key,target_timestamp]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)