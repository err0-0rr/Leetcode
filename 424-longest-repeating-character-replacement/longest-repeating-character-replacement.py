class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ls=[0]*26
        st=ord('A')
        l=r=ans=0
        n=len(s)
        while r<n:
            ls[ord(s[r])-st]+=1
            if (r-l)-max(ls)<k:
                ans=max(ans, r-l+1)
            else:
                ls[ord(s[l])-st]-=1
                l+=1
            r+=1
        return ans
        