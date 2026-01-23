# Last updated: 1/22/2026, 8:25:49 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        for num in nums:
4            while nums.count(num) > 2:
5                nums.remove(num)
6        return len(nums)