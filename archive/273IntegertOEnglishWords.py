# coding=utf-8
'''
Created on 2017Âπ?6Êú?14Êó?

@author: Administrator
'''


class Solution(object):

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "Zero"
        d1 = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
        d2 = {10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
        tens = {2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety"}
        units = ["Thousand", "Million", "Billion"]
        units_index = -1
        ans = ""
        while num:
            temp_ans = ""
            temp_num = num % 1000
            if (temp_num % 100) in d2:
                temp_ans = d2[(temp_num % 100)]  # 10,11,12,13...19
            else:
                if (temp_num % 10) in d1:
                    temp_ans = d1[(temp_num % 10)]  # ‰∏™‰Ωç
                if (temp_num % 100 / 10) in tens:
                    temp_ans = tens[temp_num % 100 / 10] + (" " if temp_ans else "") + temp_ans
            if temp_num / 100 in d1:
                temp_ans = d1[temp_num / 100] + " Hundred" + (" " if temp_ans else "") + temp_ans
            if temp_ans != "":
                temp_ans += (" " + units[units_index]) if units_index != -1 else ""
                ans = temp_ans + (" " if ans else "") + ans
            units_index += 1
            num /= 1000
#             print repr(temp_ans)
#             print repr(ans)
        return ans


s = Solution().numberToWords(1000000)
print repr(s)

