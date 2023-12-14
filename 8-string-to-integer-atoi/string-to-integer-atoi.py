class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        leng=len(s)
        if leng==0:
            return 0
        setdig={'0','1','2','3','4','5','6','7','8','9'}
        if s[0]=="-":
            flag=1
            start=1
        else:
            flag=0
            if s[0]=="+":
                start=1
            elif s[0] in setdig:
                start=0
            else:
                return 0
        end=leng    
        for i in range(start, leng):
            if s[i] not in setdig:
                end=i
                break
        #print(s, i, start, end)
        #return s[start:end+1]
        if start==end:
            return 0
        else:
            res= int(s[start:end])
            
        maxi=2**31
        if flag:
            if res>maxi:
                return -1*maxi
            else:
                return -1*res
        else:
            if res>maxi-1:
                return maxi-1
            else:
                return res
    
    
        