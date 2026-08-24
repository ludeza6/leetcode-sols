# Last updated: 8/24/2026, 9:51:44 AM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]