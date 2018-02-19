# coding=utf-8
'''
Created on 2017å¹?5æœ?28æ—?

@author: Administrator
'''


class Solution(object):

    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        for l in (list1, list2):
            for i, x in enumerate(l):
                d.setdefault(x, [])
                d[x].append(i)
        ans = []
        mini = float("inf")
        for k, v in d.items():
            if len(v) == 2:
                if sum(v) < mini:
                    ans = [k]
                    mini = sum(v)
                elif sum(v) == mini:
                    ans.append(k)
        return ans


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"]
print Solution().findRestaurant(list1, list2)
