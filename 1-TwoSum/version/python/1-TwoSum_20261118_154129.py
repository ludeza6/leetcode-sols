# Last updated: 11/18/2026, 3:41:29 PM
1class Solution:
2    def twoSum(self, nums: list[int], target: int) -> list[int]:
3        
4        seen = {}
5
6        for i, num in enumerate(nums):
7            diff = target - num
8
9            if diff in seen:
10                return [seen[diff], i]
11            
12            seen[num] = i
13
14        return []