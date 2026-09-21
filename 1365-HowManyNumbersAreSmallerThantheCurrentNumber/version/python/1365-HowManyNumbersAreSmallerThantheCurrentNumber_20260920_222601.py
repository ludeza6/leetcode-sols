# Last updated: 9/20/2026, 10:26:01 PM
1class Solution:
2    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
3        sorted_nums = sorted(nums)
4        ans = []
5        for num in nums:
6            ans.append(sorted_nums.index(num))
7        return ans