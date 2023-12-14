class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ls=[0]*len(temperatures)
        s=[]
        for i,t in enumerate(temperatures):
            while s and s[-1][1]<t:
                idx, temp=s.pop()
                ls[idx]=i-idx
            s.append((i, t))
        
        return ls 