class Solution:
    def isValid(self, s: str) -> bool:
        ls=[]
        dic={
            '}':'{',
            ']':'[',
            ')':'('
        }
        for i in s:
            if i not in dic:
                ls.append(i)
            else:
                if ls and ls[-1]==dic[i]:
                    ls.pop()
                else:
                    return False

        if not ls:
            return True
        else:
            return False