class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end={}
        for i in range(len(s)-1, -1, -1):
            if s[i] not in end:
                end[s[i]]=i
        ans=[]      
        t=set()
        tot=-1
        
        for i in range(len(s)):
            t.add(s[i])
            if i==end[s[i]]:
                t.remove(s[i])
            if not t:
                ans.append(i-tot)
                tot=i
        return ans