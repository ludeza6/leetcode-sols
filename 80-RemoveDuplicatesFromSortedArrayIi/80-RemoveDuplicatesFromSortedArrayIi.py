# Last updated: 8/6/2026, 7:30:03 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in nums:
            while nums.count(num) > 2:
                nums.remove(num)
        return len(nums)