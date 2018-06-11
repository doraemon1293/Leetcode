class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        from collections import Counter
        if len(hand) % W!=0:
            return False
        numbers=set(hand)
        counter=Counter(hand)

        while numbers:
            mini=min(numbers)
            for i in range(W):
                n=mini+i
                if n in counter:
                    counter[n]-=1
                    if counter[n]==0:
                        del counter[n]
                        numbers.remove(n)
                else:
                    return False
        return True


