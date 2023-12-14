class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        flag=False
        if n<0:
            flag=True
            n*=-1
        def Util(x, n):
            if n==0:
                return 1
            if n%2==0:
                res=Util(x, n//2)
                return res*res
                
            return x*Util(x, n-1)
        if flag:
            return 1/Util(x,n)
        return Util(x,n)