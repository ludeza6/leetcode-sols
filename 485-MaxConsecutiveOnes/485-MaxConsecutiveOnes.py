# Last updated: 11/3/2026, 10:20:53 AM
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        curr_count = 0

        for num in nums:
            if num == 1:
                curr_count += 1
            else:
                max_count = max(max_count, curr_count)
                curr_count = 0

        return max(curr_count, max_count)