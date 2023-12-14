class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ls=[]
        ans=0
        for i in range(len(heights)):
            start=i
            while ls and heights[i]<ls[-1][1]:
                ans=max(ans, ls[-1][1]*(i-ls[-1][0]))
                start=ls[-1][0]
                ls.pop()
            ls.append([start, heights[i]])
        # print(ls)
        while ls:
            ans=max(ans, ls[-1][1]*(i-ls[-1][0]+1))
            ls.pop()
            
        return ans