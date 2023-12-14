class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot=sum(nums)
        if tot%2==1:
            return False
        tot=tot//2
        s=set()
        s.add(0)
        
        for i in nums:
            temp=set()
            for j in s:
                t=i+j
                if t==tot:
                    return True
                temp.add(j)
                temp.add(t)
            s=temp
        return False