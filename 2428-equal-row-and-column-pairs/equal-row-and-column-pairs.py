class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic={}
        for i in grid:
            try:
                dic[tuple(i)]+=1
            except:
                dic[tuple(i)]=1
            
        for i in range(len(grid)):
            for j in range(i+1, len(grid)):
                grid[i][j],grid[j][i]=grid[j][i],grid[i][j]
                
        ans=0
        for i in grid:
            t=tuple(i)
            if t in dic:
                ans+=dic[t]
        return ans