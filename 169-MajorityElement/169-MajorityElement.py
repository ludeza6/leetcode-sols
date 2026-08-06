# Last updated: 8/6/2026, 7:29:52 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        limit = len(nums) // 2
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > limit:
                return num