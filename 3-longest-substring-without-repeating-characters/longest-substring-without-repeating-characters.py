class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        win_len=0
        t=set()
        
        for r in range(len(s)):
            while s[r] in t:
                t.remove(s[l])
                l+=1
            t.add(s[r])
            win_len=max(win_len, r-l+1)
            
        
        return win_len  