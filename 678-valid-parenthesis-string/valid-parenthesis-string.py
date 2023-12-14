class Solution:
    def checkValidString(self, s: str) -> bool:
        l=r=0 #range of number of left pointers possible
        
        for i in s:
            if i=='(':
                l+=1
                r+=1
            elif i==')':
                l-=1
                r-=1
            else:
                l-=1
                r+=1
            if r<0:
                return False
            if l<0:
                l=0
        if l==0:
            return True
        return False