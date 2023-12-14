class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==0:
            return []
        m=n
        matrix=[[None for i in range(m)] for j in range(n)]
        count=1
        def draw(x):
            nonlocal count
            for i in range(x, n-x):
                matrix[x][i]=count
                count+=1
            for i in range(x+1, m-x):
                matrix[i][n-x-1]=count
                count+=1
            if m-x-1!=x:
                for i in range((n-x)-2, x-1, -1):
                    matrix[m-x-1][i]=count
                    count+=1
            if x!=n-x-1:
                for i in range(m-x-2, x, -1):
                    matrix[i][x]=count
                    count+=1
            
        init=0
        while count<=n*m:
            draw(init)
            init+=1
        return matrix