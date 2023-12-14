class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro=1
        num_zero=0
        count=0
        idx=-1
        for i in nums:
            if i==0:
                num_zero+=1
                idx=count
                if num_zero>=2:
                    return [0]*len(nums)
                continue
            pro*=i
            count+=1
        if idx!=-1:
            nums=[0]*len(nums)
            nums[idx]=pro
            return nums
        for i in range(len(nums)):
                nums[i]=pro//nums[i]
        return nums