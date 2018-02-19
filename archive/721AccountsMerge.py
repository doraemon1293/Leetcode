# coding=utf-8
'''
Created on 2017å¹?11æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        d = {}  # name->accounts
        emailInd = {}  # email->ind
        for account in accounts:
            name = account[0]
            emails = set(account[1:])
            inds = set()
            for email in emails:
                if email in emailInd:
                    inds.add(emailInd[email])
            if inds:
                # todo
                minInd = min(inds)
                d[name][minInd] |= emails
                for ind in inds:
                    if ind != minInd:
                        d[name][minInd] |= d[name][ind]
                        d[name][ind] = []
                for email in d[name][minInd]:
                    emailInd[email] = minInd
            else:
                d.setdefault(name, [])
                d[name].append(emails)
                for email in emails:
                    emailInd[email] = len(d[name]) - 1
        ans = []
        for name in d:
            for account in d[name]:
                if account != []:
                    arr = sorted(account)
                    ans.append([name] + arr)
        return ans


accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
accounts = [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"], ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"], ["David", "David1@m.co", "David2@m.co"]]
accounts = [["Lily", "Lily3@m.co", "Lily4@m.co", "Lily17@m.co"], ["Lily", "Lily5@m.co", "Lily3@m.co", "Lily23@m.co"], ["Lily", "Lily0@m.co", "Lily1@m.co", "Lily8@m.co"], ["Lily", "Lily14@m.co", "Lily23@m.co"], ["Lily", "Lily4@m.co", "Lily5@m.co", "Lily20@m.co"], ["Lily", "Lily1@m.co", "Lily2@m.co", "Lily11@m.co"], ["Lily", "Lily2@m.co", "Lily0@m.co", "Lily14@m.co"]]
print Solution().accountsMerge(accounts)
