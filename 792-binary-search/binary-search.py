class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def util(i, j):
            if i>j:
                return -1
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                return util(mid+1, j)
            return util(i, mid-1)
        return util(0, len(nums)-1)
    
    