# Last updated: 11/3/2026, 10:20:51 AM
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)

        expected_sum = n * (n+1) // 2
        seen = set()

        dupe = -1
        actualsum = 0

        for num in nums:
            if num in seen:
                dupe = num
            seen.add(num)
            actualsum += num
        
        missing = expected_sum - (actualsum - dupe)
        return [dupe, missing]