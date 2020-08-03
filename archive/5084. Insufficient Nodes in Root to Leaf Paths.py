# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        to_delete = set()

        def find_to_delete(pre_sum, node):
            if node:
                pre_sum += node.val
                succ_sum = max(find_to_delete(pre_sum, node.left), find_to_delete(pre_sum, node.right))
                if succ_sum == -float("inf"):
                    succ_sum = 0
                if pre_sum + succ_sum < limit:
                    to_delete.add(node)
                print(node.val,pre_sum,succ_sum)
                return succ_sum+node.val
            else:
                return -float("inf")

        def delete(root):
            if root:
                if root.left in to_delete:
                    root.left = None
                else:
                    delete(root.left)
                if root.right in to_delete:
                    root.right = None
                else:
                    delete(root.right)

        find_to_delete(0, root)
        if root in to_delete:
            return None
        else:
            delete(root)
            return root
