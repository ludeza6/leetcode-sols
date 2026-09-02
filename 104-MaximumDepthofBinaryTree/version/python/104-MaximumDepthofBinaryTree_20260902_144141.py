# Last updated: 9/2/2026, 2:41:41 PM
1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        nums_set = set(nums)
5
6        answer = []
7
8        for i in range(1, n+1):
9            if i not in nums_set:
10                answer.append(i)
11        return answer
12