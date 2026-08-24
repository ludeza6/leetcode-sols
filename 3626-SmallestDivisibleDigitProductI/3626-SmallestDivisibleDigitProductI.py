# Last updated: 8/24/2026, 9:51:39 AM
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        while True:
            product = 1
            for digit in str(n):
                product *= int(digit)
            
            if product % t == 0:
                return n
            
            n += 1