import collections


class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.defaultdict(int)
        maxf = maxf_number = maxf_sub1_number = one_number = 0
        ans = 0
        for length, num in enumerate(nums):
            counter[num] += 1
            temp = counter[num]
            # one_number
            if temp == 1:
                one_number += 1
            if temp == 2:
                one_number -= 1
            # maxf_number and maxf_sub1_number
            if maxf < temp:
                maxf = temp
                maxf_sub1_number = max(maxf_number - 1, 0)
                maxf_number = 1
            elif maxf == temp:
                maxf_number += 1
                maxf_sub1_number = max(maxf_sub1_number - 1, 0)
            else:
                if temp == maxf - 1:
                    maxf_sub1_number += 1
            # print(num)
            # print("maxf",maxf)
            # print("maxf_number",maxf_number)
            # print("maxf_sub1_number",maxf_sub1_number)
            # print("one_number",one_number)

            if maxf == 1:
                ans = length
            else:
                if maxf_number == 1 and maxf_sub1_number == len(counter) - 1:
                    ans = length
                if maxf_number == len(counter) - 1 and one_number == 1:
                    ans = length
        return ans + 1
