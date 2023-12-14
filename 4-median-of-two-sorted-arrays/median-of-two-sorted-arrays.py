class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tot=len(nums2)+len(nums1)
        med=(tot-1)//2
        
        i,j,count=0,0,0
        while i<len(nums1) and j<len(nums2):
            if count==med:
                break
            if nums2[j]<nums1[i]:
                j+=1
            else:
                i+=1
            count+=1
        while i<len(nums1):
            if count==med:
                break
            i+=1
            count+=1
            
        while j<len(nums2):
            if count==med:
                break
            j+=1
            count+=1
            
        a=b=c=d=float("inf")
        if i!=len(nums1):
            a=nums1[i]
            if i+1!=len(nums1):
                b=nums1[i+1]
        if j!=len(nums2):
            c=nums2[j]
            if j+1!=len(nums2):
                d=nums2[j+1]
        if tot%2==1:
            return min(a,b,c,d)
        fir=min(a,c)
        sec=min(a+c-fir, b, d)
        return (fir+sec)/2