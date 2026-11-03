# Last updated: 11/3/2026, 10:20:38 AM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_nums = nums[0:n]
        y_nums = nums[n:len(nums)]

        newlist = []

        for i in range(n):
            newlist.append(x_nums[i])
            newlist.append(y_nums[i])
        return newlist