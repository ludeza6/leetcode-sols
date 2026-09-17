# Last updated: 9/17/2026, 11:00:03 AM
1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        x_nums = nums[0:n]
4        y_nums = nums[n:len(nums)]
5
6        newlist = []
7
8        for i in range(n):
9            newlist.append(x_nums[i])
10            newlist.append(y_nums[i])
11        return newlist