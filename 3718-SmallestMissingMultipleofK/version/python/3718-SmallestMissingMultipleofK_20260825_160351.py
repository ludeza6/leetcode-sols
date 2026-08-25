# Last updated: 8/25/2026, 4:03:51 PM
1class Solution:
2    def missingMultiple(self, nums: List[int], k: int) -> int:
3        count = 0
4        count += k
5        while count in nums:
6            count += k
7        return count