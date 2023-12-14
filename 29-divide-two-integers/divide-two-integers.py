class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans=int(dividend/divisor)
        # if divisor==-1 or divisor==1:
        #     ans-=1
        if ans>0:
            if ans>(2**31)-1:
                ans=(2**31)-1
        else:
            if ans<-(2**31):
                ans=-(2**31)
        return ans