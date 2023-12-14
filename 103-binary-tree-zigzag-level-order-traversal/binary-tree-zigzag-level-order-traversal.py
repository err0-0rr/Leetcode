# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag=True
        q=[]
        if root:
            q.append(root)
        ans=[]
        while q:
            fans=[]
            t=[]
            if flag:
                while q:
                    x=q.pop()
                    fans.append(x.val)
                    if x.left:
                        t.append(x.left)
                    if x.right:
                        t.append(x.right)
            else:
                while q:
                    x=q.pop()
                    fans.append(x.val)
                    if x.right:
                        t.append(x.right)
                    if x.left:
                        t.append(x.left)
            q=t
            ans.append(fans)
            flag=not flag
        return ans