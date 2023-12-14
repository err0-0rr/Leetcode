# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def util(n, s):
            if not n:
                return 0
            if n.val in s:
                s.remove(n.val)
            else:
                s.add(n.val)
            if not n.left and not n.right:
                if len(s)<=1:
                    return 1
                return 0
            
            return util(n.left, s.copy())+util(n.right, s.copy())
        return util(root, set())