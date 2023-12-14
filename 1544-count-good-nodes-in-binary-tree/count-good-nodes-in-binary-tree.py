# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def util(r, v):
            if not r:
                return 0
            if r.val>=v:
                return 1+util(r.left, r.val)+util(r.right, r.val)
            else:
                return util(r.left, v)+util(r.right, v)
        return util(root, float("-inf"))