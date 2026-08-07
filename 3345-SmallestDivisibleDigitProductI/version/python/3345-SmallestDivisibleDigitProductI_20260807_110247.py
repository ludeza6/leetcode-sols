# Last updated: 8/7/2026, 11:02:47 AM
1class Solution:
2    def smallestNumber(self, n: int, t: int) -> int:
3        
4        while True:
5            product = 1
6            for digit in str(n):
7                product *= int(digit)
8            
9            if product % t == 0:
10                return n
11            
12            n += 1