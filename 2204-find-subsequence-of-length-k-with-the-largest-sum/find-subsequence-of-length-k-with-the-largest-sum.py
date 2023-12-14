
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        def fun(x):
            return x[0]
        def fun2(x):
            return x[1]   
        n=len(nums)
        for i in range(n):
            nums[i]=(nums[i], i)
        nums.sort(key=fun)
        temp=nums[n-k:]
        temp.sort(key=fun2)
        ans=[]
        for i in temp:
            ans.append(i[0])
        return ans