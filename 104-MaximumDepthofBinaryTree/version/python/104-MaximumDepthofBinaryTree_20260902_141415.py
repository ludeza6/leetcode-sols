# Last updated: 9/2/2026, 2:14:15 PM
1class Solution:
2    def thirdMax(self, nums: List[int]) -> int:
3        nums = set(nums)
4        if len(nums) <= 2:
5            return max(nums)
6        
7        firstmax = max(nums)
8        nums.remove(firstmax)
9        secondmax = max(nums)
10        nums.remove(secondmax)
11        return max(nums)