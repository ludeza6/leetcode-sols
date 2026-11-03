# Last updated: 11/3/2026, 10:20:56 AM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        ans = []

        for i in range(1, n + 1):
            if i not in nums:
                ans += [i]

        return ans