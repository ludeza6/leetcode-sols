# Last updated: 9/2/2026, 2:30:51 PM
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) <= 2:
            return max(nums)
        
        firstmax = max(nums)
        nums.remove(firstmax)
        secondmax = max(nums)
        nums.remove(secondmax)
        return max(nums)