# Last updated: 9/17/2026, 2:00:50 PM
1class Solution:
2    def findErrorNums(self, nums: list[int]) -> list[int]:
3        n = len(nums)
4
5        expected_sum = n * (n+1) // 2
6        seen = set()
7
8        dupe = -1
9        actualsum = 0
10
11        for num in nums:
12            if num in seen:
13                dupe = num
14            seen.add(num)
15            actualsum += num
16        
17        missing = expected_sum - (actualsum - dupe)
18        return [dupe, missing]