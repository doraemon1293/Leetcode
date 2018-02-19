# coding=utf-8
'''
Created on 2017å¹?7æœ?14æ—?

@author: Administrator
'''

from collections import defaultdict


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follows = defaultdict(set)
        self.tweets = defaultdict(set)
        self.tweets_time = {}
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets[userId].add(tweetId)
        self.tweets_time[tweetId] = self.time
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        res = [(tweetId, self.tweets_time[tweetId]) for tweetId in self.tweets[userId]]
        for followeeId in self.follows[userId]:
            res.extend([(tweetId, self.tweets_time[tweetId]) for tweetId in self.tweets[followeeId]])
        res.sort(key = lambda x:x[1], reverse = True)
        return [x[0] for x in res[:10]]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.follows[followerId].discard(followeeId)


twitter = Twitter()
twitter.postTweet(1, 5)
print twitter.getNewsFeed(1)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
