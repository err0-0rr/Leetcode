class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        j=len(x)
        for i in range(0, j//2):
            if x[i]!=x[j-1]:
                return False
            else:
                j-=1
        return True