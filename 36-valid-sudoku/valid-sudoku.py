class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
                if board[i][j]!=".":
                    temp=board[i][j]
                    board[i][j]="."
                    if possible(i, j, temp):
                        board[i][j]=temp
                    else:
                        #print(i, j, temp)
                        # for i in board:
                        #     print('\t'.join(map(str, i)))
                        return False
        return True