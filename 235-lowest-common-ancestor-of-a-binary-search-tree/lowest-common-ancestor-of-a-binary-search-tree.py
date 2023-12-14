# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while not (root==p or root==q or q.val>root.val>p.val or q.val<root.val<p.val):
            if root.val>p.val:
                root=root.left
            else:
                root=root.right
        return root