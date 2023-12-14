class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxi=p=q=0
        for i in range(n):
            l=i-1
            r=i+1
            while r<n and s[r]==s[i]:
                r+=1
            while l>=0 and s[l]==s[i]:
                l-=1
            while l>=0 and r<n and s[l]==s[r]:
                r+=1
                l-=1
                
            if (r-l-1)>maxi:
                maxi=(r-l-1)
                p=l
                q=r
        return s[p+1:q]        

        