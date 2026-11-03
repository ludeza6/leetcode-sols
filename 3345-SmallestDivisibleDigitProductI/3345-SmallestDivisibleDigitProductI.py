# Last updated: 11/3/2026, 10:20:25 AM
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        while True:
            product = 1
            for digit in str(n):
                product *= int(digit)
            
            if product % t == 0:
                return n
            
            n += 1