# Last updated: 11/3/2026, 10:20:42 AM
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        ans = []
        for num in nums:
            ans.append(sorted_nums.index(num))
        return ans