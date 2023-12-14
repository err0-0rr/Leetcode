def gcd(a,b):
    while b%a!=0:
        b,a=a,b%a
    return a


class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0]!='+' and expression[0]!='-':
            expression='+'+expression
        
        num=[]
        den=[]
        i=0
        while i<len(expression):
            c=0
            if expression[i+2]=='/':
                num.append(int(expression[i+1]))
            else:
                num.append(int(expression[i+1]+expression[i+2]))
                c+=1 

            if i+4+c<len(expression) and expression[i+4+c]=='0':
                den.append(int(expression[i+3+c]+expression[i+4+c]))
                c+=1
            else:
                den.append(int(expression[i+3+c]))
            if expression[i]=='-':
                num[-1]=-num[-1]
            i+=(4+c)
        
        p,q=0,1
        for a,b in zip(num, den):
            p=(p*b)+(a*q)
            q*=b
            
        if p==0:
            return "0/1"
        hcf=gcd(q,p)
        return str(p//hcf)+'/'+str(q//hcf)