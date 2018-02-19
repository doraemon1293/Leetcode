# coding=utf-8
'''
Created on 2017å¹?2æœ?9æ—?

@author: Administrator
'''
from collections import deque


class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = deque()
        self.hits_in_300s = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if len(self.hits) == 0 or self.hits[-1][0] < timestamp:
            self.hits.append([timestamp, 1])
        else:
            self.hits[-1][1] += 1
        self.hits_in_300s += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        self.current_time = timestamp
        while self.hits and self.hits[0][0] <= timestamp - 300:
            self.hits_in_300s -= self.hits.popleft()[1]
        return self.hits_in_300s

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
