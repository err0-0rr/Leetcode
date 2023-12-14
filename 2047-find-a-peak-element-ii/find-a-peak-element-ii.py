class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        nc=len(mat[0])
        def util(l, r):
            mid=(l+r)//2
            maxi=mat[0][mid]
            cord=[0,mid]
            for i in range(len(mat)):
                if 0<=mid<nc and mat[i][mid]>maxi:
                    maxi,cord=mat[i][mid],[i, mid]
                if 0<=mid-1<nc and mat[i][mid-1]>maxi:
                    maxi,cord=mat[i][mid-1],[i, mid-1]
                if 0<=mid+1<nc and mat[i][mid+1]>maxi:
                    maxi,cord=mat[i][mid+1],[i, mid+1]
            if cord[1]==mid:
                return cord
            if cord[1]==mid-1:
                return util(l, cord[1])
            return util(cord[1], r)
            
        return util(0, nc-1)