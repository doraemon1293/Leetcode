from collections import deque


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()

        def play_deck():
            res = []
            arr = deque(list(range(len(deck))))
            while arr:
                res.append(arr.popleft())
                if arr:
                    arr.append(arr.popleft())
            return res

        arr = play_deck()
        ans = [None] * len(deck)
        for i in range(len(deck)):
            ans[arr[i]] = deck[i]
        return ans


deck = [17, 13, 11, 2, 3, 5, 7]
deck = []
print(Solution().deckRevealedIncreasing(deck))
