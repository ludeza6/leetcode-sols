# Last updated: 9/14/2026, 3:42:21 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left = 0
4        right = len(nums) - 1
5        
6        while left <= right:
7            mid = (left + right) // 2
8
9            if nums[mid] == target:
10                return mid
11            elif target < nums[mid]:
12                right = mid - 1
13
14            elif target > nums[mid]:
15                left = mid + 1
16        return -1