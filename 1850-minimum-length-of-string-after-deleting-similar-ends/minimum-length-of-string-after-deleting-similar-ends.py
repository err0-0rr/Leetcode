class Solution:
    def minimumLength(self, s: str) -> int:
        l,r=0,len(s)-1
        last_chr=''
        while l<r:
            if s[r]==s[l]:
                last_chr=s[l]
                r-=1
                l+=1
                continue
            if s[l]==last_chr:
                l+=1
                continue
            if s[r]==last_chr:
                r-=1
                continue
            break
        if l==r and s[l]==last_chr:
            return 0
        return r-l+1