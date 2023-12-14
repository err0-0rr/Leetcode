class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=0
        m=len(a)
        n=len(b)
        if m>n:
            x=m-n
            while x>0:
                b='0'+b
                x-=1
        else:
            x=n-m
            while x>0:
                a='0'+a
                x-=1
        s=""
        for i in range(max(m,n)-1, -1, -1):
            p=int(a[i])
            q=int(b[i])
            temp=p+q+c
            if temp>1:
                c=1
                s=str(temp-2)+s
            else:
                c=0
                s=str(temp)+s
        if c==1:
            return '1'+s
        return s