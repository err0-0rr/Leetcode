class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target not in set(nums):
            return False
        return True