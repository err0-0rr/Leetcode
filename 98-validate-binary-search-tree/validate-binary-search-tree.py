# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        s=float("-inf")
        ans=True
        #inorder traversal
        def util(r):
            nonlocal s
            if r.left:
                util(r.left)
            if s>=r.val:
                nonlocal ans
                ans=False
                return 
            else:
                s=r.val
            if r.right:
                util(r.right)
        util(root)
        return ans