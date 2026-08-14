# Last updated: 8/14/2026, 3:08:47 PM
1class Solution:
2    def findMissingElements(self, nums: List[int]) -> List[int]:
3        min_val = min(nums)
4        max_val = max(nums)
5
6        missing = []
7
8        for i in range(min_val, max_val, 1):
9            if i not in nums:
10                missing.append(i)
11            
12        
13        if len(missing) > 0:
14            return missing
15        
16        return missing
17