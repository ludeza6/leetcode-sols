# Last updated: 11/25/2026, 8:04:12 PM
1class Solution:
2    def sortArrayByParity(self, nums: list[int]) -> list[int]:
3        
4        even = []
5        odd = []
6        for i in range(len(nums)):
7            if nums[i] % 2 == 0:
8                even.append(nums[i])
9            else:
10                odd.append(nums[i])
11        
12        return even + odd
13