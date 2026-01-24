# Last updated: 1/24/2026, 11:03:17 AM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        counts = {}
4
5        limit = len(nums) // 2
6        for num in nums:
7            counts[num] = counts.get(num, 0) + 1
8            if counts[num] > limit:
9                return num