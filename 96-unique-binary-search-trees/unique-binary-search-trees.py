class Solution:
    def numTrees(self, n: int) -> int:
        # nth catalan number = (2n!)/((n+1)! * n!)
        num=1
        den=1
        for i in range(2*n, n+1, -1):
            num*=i
        for i in range(n, 0, -1):
            den*=i
        return num//den