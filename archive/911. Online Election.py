from collections import defaultdict
import bisect

class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        votes = defaultdict(int)
        votes[persons[0]]+=1
        max_votes=1
        lead=[[times[0],persons[0]]]
        for i in range(len(persons)):
            votes[persons[i]]+=1
            if votes[persons[i]]>=max_votes:
                lead.append([times[i],persons[i]])
                max_votes=votes[persons[i]]
         self.lead=lead



    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        ind=bisect.bisect_right(self.lead,t)
        return self.lead[ind-1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)