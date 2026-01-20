# Last updated: 1/20/2026, 2:04:54 PM
1class Solution(object):
2    def removeDuplicates(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        for num in nums:
8            if nums.count(num) > 1:
9                while nums.count(num) != 1:
10                    nums.remove(num)
11        return len(nums)