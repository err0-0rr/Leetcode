class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m=len(matrix)
        n=len(matrix[0])
        ans=[]
        def draw(x):
            if len(ans)==n*m:
                return
            for i in range(x, n-x):
                ans.append(matrix[x][i])
            for i in range(x+1, m-x):
                ans.append(matrix[i][n-x-1])
            if m-x-1!=x:
                for i in range((n-x)-2, x-1, -1):
                    ans.append(matrix[m-x-1][i])
            if x!=n-x-1:
                for i in range(m-x-2, x, -1):
                    ans.append(matrix[i][x])
            draw(x+1)
            
        draw(0)
        return ans