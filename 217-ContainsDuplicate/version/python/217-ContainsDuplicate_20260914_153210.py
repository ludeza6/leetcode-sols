# Last updated: 9/14/2026, 3:32:10 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        set_nums = set(nums)
4        return len(nums) != len(set_nums)