class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        nums=set(nums)
        def util(i, s):
            if i>=n:
                if s not in nums:
                    return s
                return ''
            
            a=util(i+1, s+'0')
            if a!='':
                return a  
            b=util(i+1, s+'1')
            if b!='':
                return b
            return ''
            
        return util(0, '')