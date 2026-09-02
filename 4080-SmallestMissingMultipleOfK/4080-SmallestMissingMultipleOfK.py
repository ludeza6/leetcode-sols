# Last updated: 9/2/2026, 2:30:43 PM
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        count = 0
        count += k
        while count in nums:
            count += k
        return count