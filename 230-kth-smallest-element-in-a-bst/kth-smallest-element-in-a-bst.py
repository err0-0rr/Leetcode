# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n=k
        ans=None
        def util(r):
            if r:
                nonlocal n
                util(r.left)
                n-=1
                if n==0:
                    nonlocal ans
                    ans=r.val
                util(r.right)
        util(root)
        return ans