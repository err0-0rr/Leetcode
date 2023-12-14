class Solution:
    def totalNQueens(self, n: int) -> int:
        ans=0
        a=[['.' for i in range(n)]for j in range(n)]
        def possible(x, y):
            for i in range(n):
                if a[x][i]=='Q' or a[i][y]=='Q':
                    return False
            i, j = x, y
            while i >= 0 and j >= 0:
                if a[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            i, j = x, y
            while i >= 0 and j < n:
                if a[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True
            
        def Util(x):
            if x==n:
                nonlocal ans
                ans=ans+1
                return
            for j in range(n):
                if possible(x, j):
                    a[x][j]='Q'
                    Util(x+1)
                    a[x][j]='.'
                    
        Util(0)      
        return ans