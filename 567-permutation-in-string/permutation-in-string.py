class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls=[0]*26
        st=ord('a')
        for i in s1:
            ls[ord(i)-st]+=1
        l,r=0,len(s1)-1
        while r<len(s2):
            ls1=ls.copy()
            for i in range(l, r+1):
                if  ls1[ord(s2[i])-st]>0:
                    ls1[ord(s2[i])-st]-=1
                else:
                    ls1[ord(s2[i])-st]+=1
                    l=l+1
                    r=l+len(s1)-1
                    break
            if i==r:
                return True
        return False