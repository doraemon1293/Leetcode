# coding=utf-8
'''
Created on 2017å¹?10æœ?3æ—?

@author: Administrator
'''


# Employee info
class Employee(object):

    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution(object):

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = {}
        for employee in employees:
            d[employee.id] = employee

        def foo(id):
            employee = d[id]
            res = employee.importance
            for i in employee.subordinates:
                res += foo(i)
            return res

        return foo(id)
