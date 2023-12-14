class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ls=[]
        temp=97
        for i in range(6):
            ls.append([chr(i+temp) for i in range(3)])
            temp+=3
        ls[5].append('s')
        ls.append(['t', 'u', 'v'])
        ls.append(['w', 'x', 'y', 'z'])
        
        ans=[]
        def util(pre, digits):
            if digits=="":
                ans.append(pre)
            else:
                for i in ls[int(digits[0])-2]:
                    util(pre+i, digits[1:])
        util("", digits)
        return ans