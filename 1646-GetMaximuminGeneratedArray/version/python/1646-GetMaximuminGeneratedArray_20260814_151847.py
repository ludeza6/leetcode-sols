# Last updated: 8/14/2026, 3:18:47 PM
1class Solution:
2    def getMaximumGenerated(self, n: int) -> int:
3        if n == 0:
4            return 0
5        nums = [0] * (n + 1)
6        nums[1] = 1
7
8        for i in range(2, n + 1, 1):
9            if i % 2 == 0:
10                nums[i] = nums[i // 2]
11            else:
12                nums[i] = nums[i // 2] + nums[i // 2 + 1]
13        return max(nums)