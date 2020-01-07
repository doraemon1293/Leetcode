class Solution:
    def maxCandies(self, status: list, candies: list, keys: list, containedBoxes: list, initialBoxes: list) -> int:
        have_boxes = set(initialBoxes)
        have_keys = set([i for i, x in enumerate(status) if x == 1])
        have_candies = 0
        can_open = have_boxes & have_candies
        while can_open:
            for i in can_open:
                have_candies += candies[i]
                have_keys = have_keys | set(keys[i])
                have_boxes = have_boxes | set(containedBoxes[i])
                have_keys.discard(i)
                have_boxes.discard()
            can_open = have_boxes & have_candies
        return have_candies
