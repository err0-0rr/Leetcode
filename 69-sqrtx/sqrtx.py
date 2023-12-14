class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l=0
        h=x
        while h-l>1:
            mid=(l+h)//2
            if mid**2>x:
                h=(l+h)//2
            else:
                l=(l+h)//2
        return l