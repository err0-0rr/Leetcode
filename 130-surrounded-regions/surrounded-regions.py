class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        def dfs(i,j, val):
            print(i,j)
            visited.add((i,j))
            val=((i,j) in s) or val
            ls=[[i-1, j], [i+1, j], [i,j-1],[i,j+1]]
            for item in ls:
                r,c=item
                if ((r,c) not in visited) and 0<=r<m and 0<=c<n and board[r][c]=='O':
                    val= dfs(r,c,val) or val
            if not val:
                board[i][j]='X'
                t.add((i,j))
            return val
        
        s=set()
        for i in range(n):
            s.add((0, i))
            s.add((m-1, i))
        for i in range(m):
            s.add((i, 0))
            s.add((i, n-1))
        visited=set()
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and (i,j) not in visited:
                    t=set()
                    temp=dfs(i,j, False)
                    if temp:
                        for x,y in t:
                            board[x][y]="O"