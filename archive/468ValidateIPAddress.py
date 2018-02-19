# coding=utf-8
'''
Created on 2017å¹?8æœ?11æ—?

@author: Administrator
'''


class Solution(object):

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        import re
        m = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", IP)
        if m:
            for s in m.groups():
                if s == "0" or s != "0" and not s.startswith("0") and int(s) <= 255:
                    pass
                else:
                    return "Neither"
            return "IPv4"
        m = re.match(r"^([0-9a-fA-F]){1,4}:([0-9a-fA-F]){1,4}:([0-9a-fA-F]){1,4}:([0-9a-fA-F]){1,4}:([0-9a-fA-F]){1,4}:([0-9a-fA-F]){1,4}:([0-9a-fA-F]){1,4}:([0-9a-fA-F]){1,4}$", IP)
        if m:
            return "IPv6"
        return "Neither"


IP = "001:0dg8:85a3:0000:0000:8a2e:0370:7334"
print Solution().validIPAddress(IP)
