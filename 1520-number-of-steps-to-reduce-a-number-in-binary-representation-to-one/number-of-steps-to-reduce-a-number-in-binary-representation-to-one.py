class Solution:
    def numSteps(self, s: str) -> int:
        s=list(s)
        ans=0
        while len(s)>1:
            ans+=1
            if s[-1]=='0':
                s.pop()
            else:
                c=1
                i=len(s)-1
                while i>=0:
                    if s[i]=='1':
                        s[i]='0'
                    else:
                        c=0
                        s[i]='1'
                        break
                    i-=1
                if c==1:
                    s.insert(0, '1')
        return ans