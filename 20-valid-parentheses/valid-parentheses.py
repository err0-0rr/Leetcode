class Solution:
    def isValid(self, s: str) -> bool:
        ls=[]
        for i in s:
            match i:
                case '(' :
                    ls.append(i)
                case '[' :
                    ls.append(i)
                case '{' :
                    ls.append(i)
                case ')':
                    if not ls or  ls[-1]!='(':
                        return False
                    else:
                        ls.pop()
                case ']':
                    if not ls or ls[-1]!='[':
                        return False
                    else:
                        ls.pop()
                case '}':
                    if not ls or ls[-1]!='{':
                        return False
                    else:
                        ls.pop()
        if not ls:
            return True
        else:
            return False