# Last updated: 11/3/2026, 10:21:07 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        return len(nums) != len(set_nums)