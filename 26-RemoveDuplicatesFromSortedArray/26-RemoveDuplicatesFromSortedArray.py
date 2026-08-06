# Last updated: 8/6/2026, 7:30:15 PM
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            if nums.count(num) > 1:
                while nums.count(num) != 1:
                    nums.remove(num)
        return len(nums)