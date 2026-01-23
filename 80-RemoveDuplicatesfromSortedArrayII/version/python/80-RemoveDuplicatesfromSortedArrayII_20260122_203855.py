# Last updated: 1/22/2026, 8:38:55 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        for i, num in enumerate(numbers):
4            remaining = target - num
5        
6            remaining_part = numbers[i + 1:] 
7            
8            if remaining in remaining_part:
9                remaining_index = remaining_part.index(remaining) + (i + 1)
10                return [i + 1, remaining_index + 1]