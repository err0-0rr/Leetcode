class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans=0
        if right:
            ans=max(ans, n-min(right))
        if left:
            ans=max(ans,max(left))
        return ans