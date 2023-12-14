class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a,b,c=0,0,0
        for i in nums:
            if i==0:
                a+=1
            elif i==1:
                b+=1
            else:
                c+=1
        nums.clear()
        nums+=[0 for _ in range(a)]+[1 for i in range(b)]+[2 for i in range(c)]