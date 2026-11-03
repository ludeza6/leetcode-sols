# Last updated: 11/3/2026, 10:21:05 AM
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        
        n = len(nums)
        set_nums = set(nums)
        for i in range(n + 1):
            if i not in set_nums:
                return i
