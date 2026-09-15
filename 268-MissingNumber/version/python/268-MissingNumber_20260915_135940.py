# Last updated: 9/15/2026, 1:59:40 PM
1class Solution:
2    def missingNumber(self, nums: list[int]) -> int:
3        
4        n = len(nums)
5        set_nums = set(nums)
6        for i in range(n + 1):
7            if i not in set_nums:
8                return i
9