class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        #print(pre,post)
        if len(pre)==0:
            return None
        else:
            val=pre[0]
            root=TreeNode(val)
            if len(pre)>1:
                val=pre[1]
                ind=post.index(val)
                new_left_post=post[:ind+1]
                new_left_pre=pre[1:ind+2]
                new_right_post=post[ind+1:-1]                
                new_right_pre=pre[ind+2:]
                root.left=self.constructFromPrePost(new_left_pre,new_left_post)
                root.right=self.constructFromPrePost(new_right_pre,new_right_post)
            return root