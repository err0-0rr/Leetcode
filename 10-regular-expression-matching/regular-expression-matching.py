class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        while len(p)>3:
            if p[0]==p[2] and p[1]==p[3]=="*":
                p=p[2:]
            else:
                break
        st=""
        for i in range(len(p)-1):
            if p[i]==p[i+1]=="*":
                continue
            else:
                st+=p[i]
        st+=p[-1]
        p=st
        return self.util(s, p, pre="")

    def util(self, s, p, pre):
        if not s:
            if not p:
                return True
            else:
                #print(s, p, pre)
                if len(p)>1 and p[1]=='*':
                    return self.util(s, p[2:], '')
                if p[0]=='*':
                    return self.util(s, p[1:], '')
                return False
            
        if not p:
            return False
            
        if p[0]=='.':
            #print("case.", s, p, pre)
            if len(p)>1 and p[1]=="*":
                return self.util(s, p[1:], '.') or self.util(s, p[2:], '')
            else:
                return self.util(s[1:], p[1:], '')
        if p[0]=='*':
            if s[0]==pre or pre=='.':
                #print("case*", s, p, pre)
                return self.util(s[1:], p, pre) or self.util(s[1:], p[1:], "")
            else:
                
                return self.util(s, p[1:], '')
        if p[0]!=s[0]:
            #print("case!=", s, p, pre)
            if len(p)<2:
                return False
            elif p[1]=='*':
                return self.util(s, p[2:], "")
            else:
                return False
        else:
            if len(p)>1 and p[1]=="*":
                return self.util(s[1:], p[1:], p[0]) or self.util(s, p[2:], p[0]) or self.util(s, p[1:], p[0])
            else:
                return self.util(s[1:], p[1:], p[0])