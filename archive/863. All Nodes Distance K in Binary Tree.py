# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        root.parent=None
        def find_target(node):
            if node==None:
                return None
            res=None
            if node==target:
                res=node
            if node.left:
                node.left.parent=node
                temp=find_target(node.left)
                if temp!=None:
                    res=temp
            if node.right:
                node.right.parent=node
                temp=find_target(node.right)
                if temp!=None:
                    res=temp
            return res
        target_node=find_target(root)

        def find_Kdistance_nodes(target_node,k,visited):
            res=[]
            visited.add(target_node)
            #print(target_node,[node.val for node in visited],k)
            if k==0:
                return [target_node]
            if target_node.parent and target_node.parent not in visited:
                res.extend(find_Kdistance_nodes(target_node.parent,k - 1,visited))
            if target_node.left and target_node.left not in visited:
                res.extend(find_Kdistance_nodes(target_node.left, k - 1,visited))
            if target_node.right and  target_node.right not in visited:
                res.extend(find_Kdistance_nodes(target_node.right, k - 1,visited))
            return res
        nodes=find_Kdistance_nodes(target_node,K,set())
        return [node.val for node in nodes]