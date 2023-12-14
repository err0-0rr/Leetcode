class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        def cor(x):
            return [x//c,  x%c]
            
        def binary(l, h):
            if l>h:
                return False
            mid=(l+h)//2
            i,j=cor(mid)
            if matrix[i][j]==target:
                return True
            if matrix[i][j]<target:
                l=mid+1
            else:
                h=mid-1
            return binary(l, h)
            
        return binary(0, r*c-1)