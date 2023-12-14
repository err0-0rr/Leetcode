class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j=m-1,n-1
        idx=i+j+1
        while idx>=0:
            if j>=0 and (nums2[j]>=nums1[i] or i<0):
                nums1[idx]=nums2[j]
                j-=1
            else:
                nums1[idx]=nums1[i]
                i-=1
            idx-=1
        return
            