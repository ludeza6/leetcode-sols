# Last updated: 1/15/2026, 11:07:27 PM
1class Solution(object):
2    def singleNumber(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        res = 0
8        for n in nums:
9            res ^= n
10        return res