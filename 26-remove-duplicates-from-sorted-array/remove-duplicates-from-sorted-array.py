class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums=len(nums)
        a=[]
        count=1
        temp=nums[0]
        a.append(temp)
        for i in range(1, len_nums):
            if temp==nums[i]:
                continue
            else:
                nums[count]=nums[i]
                temp=nums[i]
                count+=1
        return count