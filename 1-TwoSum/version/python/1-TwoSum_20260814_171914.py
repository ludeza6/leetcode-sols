# Last updated: 8/14/2026, 5:19:14 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        for i in range(len(nums)):
4            difference = target - nums[i]
5
6            if difference in nums:
7                if i == nums.index(difference):
8                    continue
9                return [nums.index(difference), i]