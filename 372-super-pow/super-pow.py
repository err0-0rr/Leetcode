class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ans = 1
        i = len(b) - 1
        y ,mod= a,1337
        while i >= 0:
            ans = (ans * pow(y, b[i], mod)) % mod
            y = pow(y, 10, mod)
            i -= 1
        return ans
        