class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        x,y=height[0],height[-1]
        maxil=[0]
        maxir=[0]
        for i in range(1,len(height)):
            x=max(x, height[i])
            maxil.append(x)
            
        for i in range(len(height)-2, -1, -1):
            y=max(y, height[i])
            maxir.insert(0,y)
            
        ans=0
        for i in range(1, len(height)-1):
            ans+=max(0, min(maxil[i], maxir[i])-height[i])
        return ans