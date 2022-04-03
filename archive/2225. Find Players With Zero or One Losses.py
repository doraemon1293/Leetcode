class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        lost_mataches = {}
        for w, l in matches:
            lost_mataches.setdefault(w, 0)
            lost_mataches.setdefault(l, 0)
            lost_mataches[l] += 1
        answer = [sorted([k for k in lost_mataches if lost_mataches[k] == 0]),
                  sorted([k for k in lost_mataches if lost_mataches[k] == 1])
                  ]
        return answer
