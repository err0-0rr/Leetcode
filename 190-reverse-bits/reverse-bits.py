class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        t=2**31
        while n:
            ans+=(t*(n%2))
            t=t//2
            n=n//2
        return ans