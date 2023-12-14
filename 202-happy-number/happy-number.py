class Solution:
    def isHappy(self, n: int) -> bool:
        def util(n):
            t=0
            while n:
                t+=(n%10)**2
                n//=10
            return t
            
        s=set()
        while n!=1:
            if n not in s:
                s.add(n)
            else:
                return False
            n=util(n)
            
        return True