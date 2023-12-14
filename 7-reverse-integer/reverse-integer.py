class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        flag=False
        if x<0:
            flag=True
            x*=-1
            
        ans=str(x)
        ans=ans[::-1]
        ans=int(ans)
        x=2**31
        if flag:
            ans= -ans
        if -x<=ans<=x-1:
            return ans
        return 0