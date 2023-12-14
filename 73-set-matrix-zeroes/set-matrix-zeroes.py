class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=set()
        c=set()
        nr=len(matrix)
        nc=len(matrix[0])
        for i in range(nr):
            for j in range(nc):
                if matrix[i][j]==0:
                    r.add(i)
                    c.add(j)
        for i in r:
            for j in range(nc):
                matrix[i][j]=0
        
        for i in c:
            for j in range(nr):
                matrix[j][i]=0 
                    