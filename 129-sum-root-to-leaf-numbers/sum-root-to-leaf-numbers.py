# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0
        def preorder(root, tot):
            if not root:
                return
            tot=tot*10+root.val
            if not root.left and not root.right:
             nonlocal ans
             ans+=tot
             return
            
            preorder(root.left, tot)
            preorder(root.right, tot)
        preorder(root, 0)
        return ans