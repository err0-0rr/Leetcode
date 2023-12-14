# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if root:
            ls=[root]
        else:
            ls=[]

        while ls:
            ans.append(ls[-1].val)
            for _ in range(len(ls)):
                temp=ls.pop(0)
                if temp.left:
                    ls.append(temp.left)
                if temp.right:
                    ls.append(temp.right)
        return ans
        