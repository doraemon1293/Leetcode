class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.nums = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number not in self.nums:
            self.nums[number] = 0
        self.nums[number] += 1
        # comment makes it slower
        # self.nums.setdefault(number, 0)
        # self.nums[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        nums = self.nums
        for num in nums:
            if (value - num) in nums and ((value - num) != num or nums[num] > 1):
                    return True
        return False
