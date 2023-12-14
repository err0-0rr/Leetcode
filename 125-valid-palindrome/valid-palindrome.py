class Solution:
    def isPalindrome(self, s: str) -> bool:
        sn = ""
        for i in s.lower():
            if i.isalnum():
                sn += i
        if sn==sn[::-1]:
            return True
        else:
            return False