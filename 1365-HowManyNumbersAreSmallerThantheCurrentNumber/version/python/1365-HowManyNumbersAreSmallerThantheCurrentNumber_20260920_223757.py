# Last updated: 9/20/2026, 10:37:57 PM
1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        nums = set(nums)
5        ans = []
6
7        for i in range(1, n + 1):
8            if i not in nums:
9                ans += [i]
10
11        return ans