class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=len(s)
        ls=["" for i in range(numRows)]
        count=row=0
        cyc=2*numRows-2
        if cyc==0:
            return s
        for i in range(n):
            ls[row]+=s[i]
            #print(row)
            if i%cyc<numRows-1:
                row+=1
            else:
                row-=1
        res=""
        for i in range(numRows):
            res+=ls[i]
        return res
        