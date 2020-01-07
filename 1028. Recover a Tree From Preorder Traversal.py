# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import re
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:

        def foo(s, depth):
            # remove refix "-"
            s = s[depth:]
            # construct root
            p = r'^\d+'
            m = re.match(p, s)
            val = int(m.group())
            root = TreeNode(val)
            # construct children
            p ="(?<!-)"+"-" * (depth + 1) + r'\d+'
            m_iter = list(re.finditer(p, s))
            # only left child
            if len(m_iter) == 1:
                m = m_iter[0]
                l_st = m.span()[0]
                root.left = foo(s[l_st:], depth + 1)
            elif len(m_iter) == 2:
                l_m, r_m = m_iter
                l_st = l_m.span()[0]
                r_st = r_m.span()[0]
                root.left = foo(s[l_st:r_st],depth + 1)
                root.right = foo(s[r_st:], depth + 1)
            return root

        return foo(S, 0)


print(Solution().recoverFromPreorder("1-2--3--4-5--6--7"))
