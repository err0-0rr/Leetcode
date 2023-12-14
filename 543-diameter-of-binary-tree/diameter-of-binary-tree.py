# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def util(head):
            if not head:
                return 0
            a=util(head.left)
            b=util(head.right)
            nonlocal ans
            ans=max(ans, a+b)
            return max(a,b)+1
        util(root)
        
        return ans

        