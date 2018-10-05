class Solution:
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        ans = 0

        def dfs(root, target):
            if root:
                return int(root.val == target) + dfs(root.left, target - root.val) + dfs(root.right, target - root.val)
            else:
                return 0

        if root:
            return dfs(root, target) + self.pathSum(root.left, target) + self.pathSum(root.right, target)
        return 0


