class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        def util(idx, i, j, s):
            if i<m and i>=0 and j<n and j>=0 and (i,j) not in s:
                if board[i][j]==word[idx]:
                    if(idx+1==len(word)):
                        return True
                    s.add((i,j))
                    return util(idx+1,i-1, j,s.copy()) or util(idx+1,i, j-1,s.copy()) or util(idx+1,i, j+1,s.copy()) or util(idx+1,i+1, j,s.copy())
            return False
        for i in range(m):
            for j in range(n):
                if util(0, i, j, set()):
                    return True
        return False