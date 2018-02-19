# coding=utf-8
'''
Created on 2016�?12�?13�?

@author: Administrator
'''


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list_to_tree(arr):
    from collections import deque
    if arr == [] or arr[0] == None:
        return None
    root = TreeNode(arr[0])
    q = deque([root])
    l_r = "left"
    for x in arr[1:]:
        node = None if x == None else TreeNode(x)
        if l_r == "left":
            q[0].left = node
            if node != None: q.append(node)
            l_r = "right"
        else:
            q[0].right = node
            if node != None: q.append(node)
            q.popleft()
            l_r = "left"
    return root


def tree_to_list(root):
    from collections import deque
    if root == None: return []
    ans = []
    q = deque([root])
    while len(q) != 0:
        node = q.popleft()
        ans.append(node.val if node else None)
        if node:
            q.append(node.left)
            q.append(node.right)
    while ans[-1] == None:
        del ans[-1]
    return ans


def inorder_traversal(root):
    arr = []

    def inorder(node):
        if node:
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

    inorder(root)
    return arr


def preorder_traversal(root):
    arr = []

    def preorder(node):
        if node:
            arr.append(node.val)
            preorder(node.left)
            preorder(node.right)

    preorder(root)
    return arr


def postorder_traversal(root):
    arr = []

    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            arr.append(node.val)

    postorder(root)
    return arr


def levelTraverseFromRoot(root):
    ans = []
    if root:
        from collections import deque
        current_level = 0
        q = deque()
        q.append((root, 0))
        temp = []
        while q:
            node, level = q.popleft()
            if level > current_level:
                ans.append(temp)
                temp = []
                current_level += 1
            temp.append(node.val)
            if node.left:
                q.append((node.left, current_level + 1))
            if node.right:
                q.append((node.right, current_level + 1))
        ans.append(temp)
    return ans


if __name__ == "__main__":
    arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    root = list_to_tree(arr)
    print (root)
    print (tree_to_list(root))
    print (inorder_traversal(root))
