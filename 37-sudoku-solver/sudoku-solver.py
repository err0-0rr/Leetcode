class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def possible(i, j, val):
            for k in range(9):
                if str(board[k][j])==val or str(board[i][k])==val:
                    return False
            r=(i//3)*3
            c=(j//3)*3
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if str(board[i][j])==val:
                        #print(i, j)
                        return False
            return True
            
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    for k in range(1, 10):
                        if possible(i, j, str(k)):
                            board[i][j]=str(k)
                            if self.solveSudoku(board):
                                return True
                            board[i][j]='.'
                    return False
        return True      