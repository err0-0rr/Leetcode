class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def util(i, j, k):
            if k==len(s3):
                if i==len(s1) and j==len(s2):
                    return True
                return False
            if (i, j) in mem:
                return mem[(i,j)]
            a=False
            b=False
            if i<len(s1) and s1[i]==s3[k]:
                a=util(i+1, j, k+1)
            if j<len(s2) and s2[j]==s3[k]:
                b=util(i, j+1, k+1)
            mem[(i,j)]= a or b
            return a or b
            mem[(i,j)]=a or b
        mem={}
        return util(0,0,0)