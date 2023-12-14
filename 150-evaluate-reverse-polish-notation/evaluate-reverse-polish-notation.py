class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            #print(s)
            if i=='+':
                s.append(s.pop()+s.pop())
            elif i=='-':
                s.append(-1*(s.pop()-s.pop()))
            elif i=='*':
                s.append(s.pop()*s.pop())
            elif i=='/':
                b=s.pop()
                a=s.pop()
                s.append(int(a/b))
            else:
                s.append(int(i))
        return s[-1]
        