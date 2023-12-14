class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        s1=set()
        def long(x):
            count=1
            i=x+1
            while i in s:
                s1.add(i)
                count+=1
                i+=1
            i=x-1
            while i in s:
                s1.add(i)
                count+=1
                i-=1
            return count
        ans=0
        for i in nums:
            if i in s1:
                continue
            ans=max(ans, long(i))
            
        return ans
        