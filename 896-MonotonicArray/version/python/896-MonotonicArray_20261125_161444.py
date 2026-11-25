# Last updated: 11/25/2026, 4:14:44 PM
1class Solution:
2    def isMonotonic(self, nums: list[int]) -> bool:
3        sorted_nums = sorted(nums)
4        if sorted_nums == nums or sorted_nums[::-1] == nums:
5            return True
6        return False