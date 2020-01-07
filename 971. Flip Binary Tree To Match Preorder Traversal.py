# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        ans = []

        def solve(root, voyage):
            print(root.val,voyage)
            if root.val != voyage[0]:
                return False
            if root.left:
                left_ind = -1 if root.left.val not in voyage else voyage.index(root.left.val)
            else:
                left_ind = None
            if root.right:
                right_ind = -1 if root.right.val not in voyage else voyage.index(root.right.val)
            else:
                right_ind = None
            if left_ind == -1 or right_ind == -1:
                return False
            if left_ind == right_ind == None:
                if len(voyage) == 1:
                    return True
                else:
                    return False
            if left_ind == None:
                if right_ind == 1:
                    return solve(root.right, voyage[right_ind:])
                else:
                    return False
            if right_ind == None:
                if left_ind == 1:
                    return solve(root.left, voyage[left_ind:])
                else:
                    return False
            if left_ind != None and right_ind != None:
                if left_ind == 1:
                    left = solve(root.left, voyage[left_ind:right_ind])
                    right = solve(root.right, voyage[right_ind:])
                    return left and right
                elif right_ind == 1:
                    ans.append(root.val)
                    right = solve(root.right, voyage[right_ind:left_ind])
                    left = solve(root.left, voyage[left_ind:])
                    return left and right
                else:
                    return False

        if solve(root,voyage):
            return ans
        else:
            return [-1]
