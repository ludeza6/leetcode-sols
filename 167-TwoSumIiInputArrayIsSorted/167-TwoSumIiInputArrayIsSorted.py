# Last updated: 8/6/2026, 7:29:54 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            remaining = target - num
        
            remaining_part = numbers[i + 1:] 
            
            if remaining in remaining_part:
                remaining_index = remaining_part.index(remaining) + (i + 1)
                return [i + 1, remaining_index + 1]