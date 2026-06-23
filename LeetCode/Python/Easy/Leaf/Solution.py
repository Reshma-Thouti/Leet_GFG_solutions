# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res=[]
        def fun(root):
            if root:
                if not root.left and not root.right:
                    res.append(root.val)
                fun(root.left)
                fun(root.right)
            return res
        x=fun(root1)
        res=[]
        y=fun(root2)
        return x==y