class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def util(l, h):
            #print(l, h)
            if l>h:
                return -1
            mid=(l+h)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[l]:
                if target<nums[mid] and target>=nums[l]:
                    return util(l, mid-1)
                else:
                    return util(mid+1, h)
            else:
                if target>nums[mid] and target<=nums[h]:
                    return util(mid+1, h)
                else:
                    return util(l, mid-1)
                
        return util(0, len(nums)-1)