# coding=utf-8
'''
Created on 2017�?1�?8�?

@author: Administrator
'''
#
#
# class BinarySearchTree(object):
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#
# def find(self, x):
#     if x == self.key:
#         return self
#     elif x < self.key and self.left:
#         return self.left.find(x)
#     elif x > self.key and self.right:
#         return self.right.find(x)
#     else:
#         return None
#
# def findMin(self):
#     if self.left:
#         return self.left.findMin()
#     else:
#         return self
# def findMax(self):
#     if self.right:
#         return self.right.findMax()
#     else:
#         return self
#
# def delete(self, x):
#     if self.find(x):
#         if x < self.key:
#             self.left = self.left.delete(x)
#             return self
#         elif x > self.key:
#             self.right = self.right.delete(x)
#             return self
#         elif self.left and self.right:
#             key = self.right.findMin().key
#             self.key = key
#             self.right = self.right.delete(key)
#             return self
#         else:
#             if self.left:
#                 return self.left
#             else:
#                 return self.right
#     else:
#         return self


# Another
class TreeNode(object):

    def __init__(self, key, left = None, right = None, parent = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self


class BSTree(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def insert(self, x):
        node = TreeNode(x)
        if not self.root:
            self.root = node
            self.size += 1
        else:
            currentNode = self.root
            while True:
                if x < currentNode.key:
                    if currentNode.left:
                        currentNode = currentNode.left
                    else:
                        currentNode.left = node
                        node.parent = currentNode
                        self.size += 1
                        break
                elif x > currentNode.key:
                    if currentNode.right:
                        currentNode = currentNode.right
                    else:
                        currentNode.right = node
                        node.parent = currentNode
                        self.size += 1
                        break
                else:
                    break

    def find(self, key):
        if self.root:
            res = self._find(key, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def _find(self, key, node):
        if not node:
            return None
        elif node.key == key:
            return node
        elif key < node.key:
            return self._find(key, node.left)
        else:
            return self._find(key, node.right)

    def findMin(self):
        if self.root:
            current = self.root
            while current.left:
                current = current.left
            return current
        else:
            return None

    def _findMin(self, node):
        if node:
            current = node
            while current.left:
                current = current.left
            return current

    def findMax(self):
        if self.root:
            current = self.root
            while current.right:
                current = current.right
            return current
        else:
            return None

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self.find(key)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError, 'Error, key not in tree'
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, node):
        if not node.left and not node.right:  # node为树�?
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None

        elif node.left and node.right:  # 有两个儿�?
            minNode = self._findMin(node.right)
            node.key = minNode.key
            self.remove(minNode)

        else:  # 有一个儿�?
            if node.hasLeftChild():
                if node.isLeftChild():
                    node.left.parent = node.parent
                    node.parent.left = node.left
                elif node.isRightChild():
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:  # node为根
                    self.root = node.left
                    node.left.parent = None
                    node.left = None
            else:
                if node.isLeftChild():
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.isRightChild():
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:  # node为根
                    self.root = node.right
                    node.right.parent = None
                    node.right = None
