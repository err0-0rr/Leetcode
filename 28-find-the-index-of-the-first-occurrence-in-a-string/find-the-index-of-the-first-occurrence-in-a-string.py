class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #Used KMP for string matching
        j=0
        i=1
        n=len(needle)
        ans=-1
        #Uses KMP
        ls=[0 for i in range(n)]
        while i<n:
            if needle[j]==needle[i]:
                ls[i]=j+1
                j+=1
                i+=1
            else:
                if j==0:
                    i+=1
                else:
                    j=ls[j-1]
        #print(ls)
        m=len(haystack)
        i=0
        j=0
        while i<m:
            if haystack[i]==needle[j]:
                i+=1
                j+=1
                if j==n:
                    ans=i-j
                    break
            else:
                if j==0:
                    i+=1
                else:
                    j=ls[j-1]
        return ans