# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def util(a, b):
            if not a or not b or a.val!=b.val:
                return False
            x,y=True,True
            if a.left or b.left:
                if not util(a.left, b.left):
                    return False
            if a.right or b.right:
                if not util(a.right, b.right):
                    return False
            return True
        if not p and not q:
            return True
        return util(p, q)