# Last updated: 11/3/2026, 10:20:26 AM
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        count = 0
        count += k
        while count in nums:
            count += k
        return count