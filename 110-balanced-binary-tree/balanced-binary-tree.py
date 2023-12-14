# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def util(head):
            if not head:
                return (True, 0)
            b1,h1=util(head.left)
            b2,h2=util(head.right)
            if b1 and b2 and -2<h1-h2<2:
                return (True, max(h1, h2)+1)
            else:
                return (False, max(h1, h2)+1)
        ans,h=util(root)
        return ans