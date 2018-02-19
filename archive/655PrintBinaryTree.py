# coding=utf-8
'''
Created on 2017å¹?8æœ?6æ—?

@author: Administrator
'''
from data_structure.Tree import list_to_tree


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if root == None:
            return []

        def levelTraverseFromRoot(root):
            ans = [[root]]
            flag = True
            while flag:
                flag = False
                temp = []
                for node in ans[-1]:
                    left = node.left if node else None
                    right = node.right if node else None
                    temp.append(left)
                    temp.append(right)
                    if left != None or right != None:
                        flag = True
                if flag: ans.append(temp)
            return ans

        ans = levelTraverseFromRoot(root)
        ans = [[str(node.val) if node else "" for node in row] for row in ans]
        level = len(ans)
        nodes_count = 2 ** level - 1
        inds = [nodes_count / 2]
        res = [[""] * (2 ** level - 1) for _ in xrange(level)]
        for i, row in enumerate(ans):
            for j, node in enumerate(row):
                res[i][inds[j]] = node
            new_inds = []
            temp = 2 ** (level - i - 2)
            for ind in inds:
                new_inds.append(ind - temp)
                new_inds.append(ind + temp)
            inds = new_inds
        return res


root = list_to_tree([1, 2, 5, 3, None, None, None, 4])
print Solution().printTree(root)

