# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def util(head):
            if head:
                util(head.left)
                ans.append(head.val)
                util(head.right)
        ans=[]
        util(root)
        return ans
        