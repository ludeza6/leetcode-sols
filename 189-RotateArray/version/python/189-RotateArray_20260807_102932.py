# Last updated: 8/7/2026, 10:29:32 AM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        if not nums:
7            return
8        
9        k = k % len(nums)
10        nums[:] = nums[-k:] + nums[:-k]