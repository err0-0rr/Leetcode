# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def tot(r):
    if not r:
        return 0
    return 1+tot(r.left)+tot(r.right)
    

class Solution:
    def btreeGameWinningMove(self, root:TreeNode, n: int, x: int) -> bool:
        def util(r):
            if not r:
                return None
            if r.val==x:
                l=tot(r.left)
                r=tot(r.right)
                return min(l+r+1, n-max(l,r))
            
            a=util(r.left)
            if a:
                return a
            b=util(r.right)
            if b:
                return b
            
            return None
        
        #x:extra on first player, y:max second can get; sec:sec player in full half    
        # fir=None
        # sec=None
        # if root.val==x:
        #     l=tot(root.left)
        #     r=tot(root.right)
        #     fir=min(l,r)+1
        #     sec=n-fir
        # else:
        #     fir=util(root)
        #     sec=n-fir
        # return sec>fir
        fir=util(root)
        return (n-fir)>fir