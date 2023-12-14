# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        h=self.height(root, 0)
        ans=[[] for _ in range(h)]
        def dfs(r, h):
            nonlocal ans
            if r:
                ans[h].append(r.val)
                dfs(r.left, h+1)
                dfs(r.right, h+1)
        dfs(root, 0)
        return ans
            
        
        
    def height(self, r, h):
        if not r:
            return h
        return max(self.height(r.left, h+1), self.height(r.right, h+1))