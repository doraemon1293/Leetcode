# coding=utf-8
'''
Created on 17 Jan 2018

@author: Administrator
'''


class Solution:

    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        import math

        def ipToInt(ip):
            n = 0
            for x in ip.split("."):
                x = int(x)
                n *= 256
                n += x
            return n

        def intToIp(n):
            ip = []
            for _ in range(4):
                ip.append(n % 256)
                n //= 256
            return ".".join([str(x) for x in ip[::-1]])

        def tailZero(n):
            res = 0
            while n and n % 2 == 0:
                res += 1
                n //= 2
            return res

        curIpN = ipToInt(ip)
        ans = []
        while n:
            zeros = tailZero(curIpN)
            while 2 ** zeros > n:
                zeros -= 1
            ans.append(intToIp(curIpN) + "/" + str(32 - zeros))
            curIpN += 2 ** zeros
            n -= 2 ** zeros

        return ans


ip = "230.255.255.255"
n = 0
ip = "255.0.0.8"
n = 7
print(Solution().ipToCIDR(ip, n))

