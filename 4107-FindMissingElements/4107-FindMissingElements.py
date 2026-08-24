# Last updated: 8/24/2026, 9:51:40 AM
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_val = min(nums)
        max_val = max(nums)

        missing = []

        for i in range(min_val, max_val, 1):
            if i not in nums:
                missing.append(i)
            
        
        if len(missing) > 0:
            return missing
        
        return missing
